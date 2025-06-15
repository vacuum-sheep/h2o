import os
import glob
import re
import csv

# 设定根目录
root_dir = "/home/kaiwen/H2O/h2o_hf/outputs_sweep"
output_csv = "all_rouge_scores.csv"

# 宽松正则，匹配 rouge-1/2/l
rouge_line_re = re.compile(
    r"rouge-1:\s*([0-9.]+),\s*rouge-2:\s*([0-9.]+),\s*rouge-l:\s*([0-9.]+)"
)

records = []
txt_files = glob.glob(f"{root_dir}/*/*/ratio_*/result.jsonl")

print(f"🔍 Found {len(txt_files)} result.jsonl files")

for txt_file in txt_files:
    print(f"📄 Parsing: {txt_file}")
    try:
        parts = txt_file.split(os.sep)
        dataset = parts[-4]
        mode = parts[-3]
        ratio_str = parts[-2].replace("ratio_", "")
        ratio = float(ratio_str)

        with open(txt_file, "r") as f:
            for line in reversed(f.readlines()):
                match = rouge_line_re.search(line)
                if match:
                    rouge1 = float(match.group(1))
                    rouge2 = float(match.group(2))
                    rougel = float(match.group(3))
                    records.append([dataset, mode, ratio, rouge1, rouge2, rougel])
                    break
            else:
                print(f"❌ No ROUGE line found in {txt_file}")
    except Exception as e:
        print(f"⚠️ Error parsing {txt_file}: {e}")

# 写入 CSV
with open(output_csv, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["dataset", "mode", "ratio", "rouge-1", "rouge-2", "rouge-l"])
    writer.writerows(records)

print(f"✅ Collected {len(records)} records into {output_csv}")
