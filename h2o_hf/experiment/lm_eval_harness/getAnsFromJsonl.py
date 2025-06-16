import json

jsonl_path = "openbookqa-5-llama-hr0.3_rr0.3.jsonl"

# 用于存储每行的模型输出
answers = []

with open(jsonl_path, "r") as f:
    for line in f:
        obj = json.loads(line)
        try:
            text = obj["result"]["choices"][0]["text"]
            answers.append(text.strip())
        except KeyError:
            print("Warning: Missing output in line")

# 打印前 5 个答案
for i, a in enumerate(answers[:10]):
    print(f"[{i}] {a}\n")
