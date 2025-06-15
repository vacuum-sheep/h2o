import os
import subprocess
from itertools import product

# 基础路径设置
script = "run_summarization.py"  # 你要跑的主脚本
output_base = "outputs_sweep"    # 所有实验的结果都会保存在这个文件夹下
os.makedirs(output_base, exist_ok=True)

# Sweep 参数空间定义
datasets = ["xsum"]
cache_modes = ["full", "local", "h2o"]
ratios = [1.0, 0.8, 0.6, 0.4, 0.2, 0.01]
sample_num = 50 # 每个实验取样的数量（可调）

# Sweep 参数空间定义
# datasets = ["xsum"]
# cache_modes = ["full"]
# ratios = [1.0, 0.8, 0.6, 0.4, 0.2, 0.01]
# sample_num = 50  # 每个实验取样的数量（可调）

# 路径模板（假设你已有 xsum.jsonl）
input_paths = {
    "xsum": "data/xsum.jsonl",
}

# 主循环跑 sweep
for dataset, mode, ratio in product(datasets, cache_modes, ratios):
    if mode == "full" and ratio != 1.0:
        continue  # full 模式下 ratio 固定为1.0，只跑一次

    # 构建输出路径
    out_dir = f"{output_base}/{dataset}/{mode}/ratio_{ratio:.2f}"
    os.makedirs(out_dir, exist_ok=True)
    output_path = os.path.join(out_dir, "result.jsonl")

    # 构建运行命令
    cmd = [
        "python", script,
        "--input_path", input_paths[dataset],
        "--output_path", output_path,
        "--model_name", "huggyllama/llama-7b",  # 根据你实际情况改
        "--sample_num", str(sample_num),
        "--batch_size", "1",
    ]

    if mode != "full":
        cmd += [
            "--enable_h2o_cache" if mode == "h2o" else "",
            "--hh_size", str(int(ratio * 2048)),
            "--recent_size", str(int(ratio * 2048)),
        ]

    print(f"\n>>> Running: {cmd}\n")
    subprocess.run([c for c in cmd if c != ""], check=True)
