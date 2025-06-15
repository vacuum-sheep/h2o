#!/usr/bin/env python3
"""
生成一个 512 token 的占位 prompt，并写成 MT-Bench 格式的 jsonl：
{"turns": ["<512_tokens_text>"]}
"""
import json, argparse, os

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tokens", type=int, default=512)
    ap.add_argument("--word",   type=str, default="hello")
    ap.add_argument("--out",    type=str, default="data/custom_mt.jsonl")
    args = ap.parse_args()

    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    text = " ".join([args.word]*args.tokens)
    with open(args.out, "w") as f:
        json.dump({"turns": [text]}, f)
        f.write("\n")
    print(f"[OK] Wrote {args.out} with {args.tokens} tokens.")

if __name__ == "__main__":
    main()
