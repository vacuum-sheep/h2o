import json, re, sys
import numpy as np

def load(path): return [json.loads(l) for l in open(path)]

def extract_boxed(text):
    m = re.search(r"\\boxed{([^}]*)}", text)
    return m.group(1).strip() if m else None

gt = {j["ID"]: str(j["Answer"]) for j in map(json.loads, open("experiment/aime24/AIME24.jsonl"))}

def acc(pred_path):
    ok = 0; total = 0
    for item in load(pred_path):
        pid = item["request"]["id"]
        out = item["result"]["choices"][0]["text"]
        ans = extract_boxed(out)
        if ans is not None:
            print(ans)
            ok += (ans == gt[pid])
            total += 1
    return ok/total if total else 0.0, total

for tag in ["full", "h2o"]:
    acc_val, n = acc(f"experiment/aime24/aime24_{tag}.jsonl")
    print(f"{tag:<5}  n={n:3d}  accuracy={acc_val:.3f}")
