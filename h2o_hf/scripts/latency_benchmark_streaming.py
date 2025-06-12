#!/usr/bin/env python3
"""
一次跑三种 max_gen_len，打印吞吐率。
"""
import subprocess, argparse, os, json, time

def run(length):
    cmd = [
        "python", "run_streaming.py",
        "--model_name_or_path", "huggyllama/llama-7b",
        "--data_root", "data",
        "--enable_streaming_with_H2O",
        "--heavy_hitter_size", "4",
        "--recent_size", "2000",
        "--max_gen_len", str(length),          # ← 需要在 run_streaming.py 里把该参数加到 argparse
    ]
    print("\n\n=== Running max_gen_len =", length, "===")
    subprocess.run(cmd, check=True)

def main():
    for L in (32, 512, 1024):
        run(L)

if __name__ == "__main__":
    main()
