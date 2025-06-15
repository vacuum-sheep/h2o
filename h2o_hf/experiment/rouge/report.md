Under llama7b, test bechmark(measuring in ) of xsum under 0.01, 0.2, 0.4, 0.6, 0.8, 1.0 kv cache budget with full,local, h2o strategy.

based on run_summarizaion.py,  sample_size: 50
equivalent to figure4: llama7b+xsum

1. Run Full kvcache as baseline:
bash scripts/summarization/eval.sh xsum ${shots} full ${GPU-ID}
shots = 3
GPU-ID = 0

Average Rouge Score:
rouge-1: 0.285860, rouge-2: 0.101519, rouge-l: 0.242009

Detailed Output:
xsum_3shot_full.jsonl

2. H2O
Constant H2 size and recent token size:
我们取 sample的 average input token length T 作为参考，20% kv cache budget就是 0.2T, HH size: 0.1T, recent size: 0.1T
T:1421, 获取： embedded in run_summarization.py

run_h2o_batch.sh: 

Average Rouge Score:
0.01: rouge-1: 0.048972, rouge-2: 0.004506, rouge-l: 0.042612
0.2: rouge-1: 0.289918, rouge-2: 0.106479, rouge-l: 0.246726
0.4: rouge-1: 0.277361, rouge-2: 0.100236, rouge-l: 0.230968
0.6: rouge-1: 0.284314, rouge-2: 0.102259, rouge-l: 0.240533
0.8: rouge-1: 0.290221, rouge-2: 0.101888, rouge-l: 0.243631
1.0: rouge-1: 0.284229, rouge-2: 0.103332, rouge-l: 0.240360

Detailed Output:
xsum_3shot_h2o_hhxsum_local3.jsonl

3. local
Constant recent token size:
同上， T:1421

run_local_batch.sh: 

Average Rouge Score:
0.01: rouge-1: 0.016519, rouge-2: 0.000000, rouge-l: 0.016519
0.2: rouge-1: 0.011504, rouge-2: 0.000000, rouge-l: 0.011504
0.4: rouge-1: 0.015901, rouge-2: 0.000000, rouge-l: 0.015901
0.6: rouge-1: 0.013682, rouge-2: 0.000000, rouge-l: 0.013682
0.8: rouge-1: 0.133891, rouge-2: 0.050677, rouge-l: 0.121051
1.0: rouge-1: 0.202502, rouge-2: 0.074832, rouge-l: 0.178870

Detailed Output:
xsum_3shot_h2o_hhxsum_local3.jsonl
