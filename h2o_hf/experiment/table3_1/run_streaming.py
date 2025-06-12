import warnings

warnings.filterwarnings("ignore")

import torch
import argparse
import json
import os
import time
import re
import sys

from tqdm import tqdm
#from streaming_llm.utils import load, download_url, load_jsonl
from utils_real_drop.stream import load, download_url, load_jsonl

from transformers.models.llama.modeling_llama import LlamaAttention
from utils_real_drop.modify_llama import H2OLlamaAttention_streaming, H2OLlamaForCausalLM_streaming

@torch.no_grad()
# past_key_values 就是那个 kv cache
def greedy_generate(model, tokenizer, input_ids, past_key_values, max_gen_len, measure:dict = None):
    """
    Streaming greedy decoding + 吞吐率统计。
    `measure` 是 dict：{"gen_tokens": 0, "seconds": 0}
    """
    if measure is None:
        measure = {"gen_tokens": 0, "seconds": 0}

    t0 = time.time()

    # prefill
    outputs = model(
        input_ids=input_ids,
        past_key_values=past_key_values,
        use_cache=True,
    )
    # 处理 prefill 结果
    past_key_values = outputs.past_key_values
    pred_token_idx = outputs.logits[:, -1, :].argmax(dim=-1).unsqueeze(1)

    '''generated_ids 用于保存每一个 token id，后续用于 decode 成人类可读文本。pos 用于追踪“打印到哪一段了”。
		不生成文本结果，只测试生成速度，不需要 generated_ids。
		pos 仅用于输出字符串片段，对吞吐率无用。'''
    # generated_ids = [pred_token_idx.item()]
    # pos = 0

    # token by token 的 streaming 推理
    for _ in range(max_gen_len - 1):
        outputs = model(
            input_ids=pred_token_idx,
            past_key_values=past_key_values,
            use_cache=True,
        )
        past_key_values = outputs.past_key_values
        pred_token_idx = outputs.logits[:, -1, :].argmax(dim=-1).unsqueeze(1)

        # 逐 token 地拼出完整句子（使用 .decode()），并边生成边打印出来。 但 tokenizer.decode， print() I/O 等都会大幅影响时间统计，不该算进推理性能的计时里
        # generated_ids.append(pred_token_idx.item())
        # generated_text = (
        #     tokenizer.decode(
        #         generated_ids,
        #         skip_special_tokens=True,
        #         clean_up_tokenization_spaces=True,
        #         spaces_between_special_tokens=False,
        #     )
        #     .strip()
        #     .split(" ")
        # )

        # now = len(generated_text) - 1
        # if now > pos:
        #     print(" ".join(generated_text[pos:now]), end=" ", flush=True)
        #     pos = now

        # 累计token个数
        measure["gen_tokens"] += 1

        # 判断是否提前结束
        if pred_token_idx == tokenizer.eos_token_id:
            break

    # print(" ".join(generated_text[pos:]), flush=True)
    measure["seconds"] += time.time() - t0
    return past_key_values

@torch.no_grad()
def streaming_inference(model, tokenizer, prompts, kv_cache=None, max_gen_len=1000):
    past_key_values = None
    for idx, prompt in enumerate(prompts):
        prompt = "USER: " + prompt + "\n\nASSISTANT: "
        print("\n" + prompt, end="")
        input_ids = tokenizer(prompt, return_tensors="pt").input_ids
        input_ids = input_ids.to(model.device)
        seq_len = input_ids.shape[1]
        if kv_cache is not None:
            space_needed = seq_len + max_gen_len
            past_key_values = kv_cache.evict_for_space(past_key_values, space_needed)

        past_key_values = greedy_generate(
            model, tokenizer, input_ids, past_key_values, max_gen_len=max_gen_len
        )

@torch.no_grad()
def streaming_inference_heavy_hitter(model, tokenizer, prompts, kv_cache=None, max_gen_len=1000):
    past_key_values = None
    for idx, prompt in enumerate(prompts):
        prompt = "USER: " + prompt + "\n\nASSISTANT: "
        print("\n" + prompt, end="")
        input_ids = tokenizer(prompt, return_tensors="pt").input_ids
        input_ids = input_ids.to(model.device)
        seq_len = input_ids.shape[1]
        if kv_cache is not None:
            space_needed = seq_len + max_gen_len

            for name, m in model.named_modules():
                if isinstance(m, H2OLlamaAttention):
                    layer_idx = int(name.split(".")[2])
                    past_key_values[layer_idx] = m.kv_cache.evict_for_space(past_key_values[layer_idx], space_needed)   
        measure = {"gen_tokens": 0, "seconds": 0}
        past_key_values = greedy_generate(
            model, tokenizer, input_ids, past_key_values, max_gen_len=max_gen_len, measure=measure
        )
        print(measure["gen_tokens"]/measure["seconds"])


def main(args):
    model_name_or_path = args.model_name_or_path
    model, tokenizer = load(model_name_or_path, args.enable_streaming_with_H2O, args)
    test_filepath = os.path.join(args.data_root, "mt_bench.jsonl")
    print(f"Loading data from {test_filepath} ...")

    if not os.path.exists(test_filepath):
        download_url(
            "https://raw.githubusercontent.com/lm-sys/FastChat/main/fastchat/llm_judge/data/mt_bench/question.jsonl",
            args.data_root,
        )
        os.rename(os.path.join(args.data_root, "question.jsonl"), test_filepath)

    list_data = load_jsonl(test_filepath)
    prompts = []
    for sample in list_data:
        prompts += sample["turns"]

    if args.enable_streaming_with_H2O:
        kv_cache = None
        streaming_inference_heavy_hitter(
            model,
            tokenizer,
            prompts,
            kv_cache,
            max_gen_len=args.max_gen_len
        )

    else:
        kv_cache = None
        streaming_inference(
            model,
            tokenizer,
            prompts,
            kv_cache,
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--model_name_or_path", type=str, default="lmsys/vicuna-13b-v1.3"
    )
    parser.add_argument("--data_root", type=str, default="data/")
    parser.add_argument("--enable_streaming_with_H2O", action="store_true")
    parser.add_argument("--start_size", type=int, default=4)
    parser.add_argument("--heavy_hitter_size", type=int, default=4)
    parser.add_argument("--recent_size", type=int, default=2000)

    # For testing latency
    parser.add_argument("--max_gen_len", type=int, default=512)

    args = parser.parse_args()

    main(args)
