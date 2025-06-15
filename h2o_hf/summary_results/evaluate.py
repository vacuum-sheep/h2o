import json
from rouge import Rouge
from tqdm import tqdm

# 你的 JSONL 文件
# input_file = 'summary_results/xsum_3shot_full.jsonl'
input_file = 'generate_xsum_llama7b.jsonl'

generated_summaries = []
reference_summaries = []

with open(input_file, 'r') as f:
    for line in tqdm(f):
        obj = json.loads(line)
        gen = obj["result"]["choices"][0]["text"].strip()
        ref = obj["request"]["summary_gt"].strip()
        generated_summaries.append(gen)
        reference_summaries.append(ref)

rouge = Rouge()
scores = rouge.get_scores(generated_summaries, reference_summaries, avg=True)

print("=== Benchmark Result ===")
print("ROUGE-1: {:.4f}".format(scores["rouge-1"]["f"]))
print("ROUGE-2: {:.4f}".format(scores["rouge-2"]["f"]))
print("ROUGE-L: {:.4f}".format(scores["rouge-l"]["f"]))
