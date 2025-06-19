''' 将aime24.jsonl 转换成 H2O* 的 “request-格式 '''
import json, sys, uuid

TEMPLATE = "Problem: {question}\nLet's solve step-by-step. " \
           "Give the final numeric answer enclosed in \\boxed{{}}, like \\boxed{{42}}."

out = open("experiment/aime24/aime24_requests.jsonl", "w")
for line in open("experiment/aime24/AIME24.jsonl"):
    item = json.loads(line)
    req = {
        "id": item["ID"],
        "prompt": TEMPLATE.format(question=item["Question"]),
        # 下三行是 run_lm_eval_harness.py 需要的字段
        "temperature": 0.0,
        "top_p": 1.0,
        "n": 1,
        # 生成长度预估（再长也不会超过 512）
        "max_tokens": 512,
        "stop": ["</s>"]       # 生成到换行就停
    }
    out.write(json.dumps(req) + "\n")
out.close()


