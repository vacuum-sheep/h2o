from datasets import load_dataset
import json

# 控制总采样量（可以按论文 100-500 条）
num_samples = 100

# 生成 jsonl 文件的辅助函数
def dump_to_jsonl(samples, path, max_tokens=64):
    with open(path, "w") as f:
        for sample in samples:
            line = {
                "article": sample["document"],
                "summary_gt": sample["summary"],
                "temperature": 1.0,
                "top_p": 1.0,
                "stop": ["</s>"],
                "max_tokens": max_tokens,
                "n": 1
            }
            f.write(json.dumps(line) + "\n")

# 1. XSUM
xsum_dataset = load_dataset("xsum", split="test[:{}]".format(num_samples))
xsum_samples = [{"document": d["document"], "summary": d["summary"]} for d in xsum_dataset]
dump_to_jsonl(xsum_samples, "xsum.jsonl", max_tokens=64)
