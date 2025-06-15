Reproducing Fig4 experiment under llama7b+xsum

settings difference: opt6.7b -> llama7b, T4 GPU-> two 3090 GPU

(h2o_env) kaiwen@Projgpu26:~/H2O/h2o_hf/result$ nvidia-smi
Thu Jun 12 13:52:34 2025       
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 575.57.08              Driver Version: 575.57.08      CUDA Version: 12.9     |
|-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA GeForce RTX 3090        Off |   00000000:18:00.0 Off |                  N/A |
| 30%   52C    P0            107W /  350W |       0MiB /  24576MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
|   1  NVIDIA GeForce RTX 3090        Off |   00000000:8A:00.0 Off |                  N/A |
| 30%   42C    P0            109W /  350W |       0MiB /  24576MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
                                                                                         
+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|  No running processes found                                                             |
+-----------------------------------------------------------------------------------------+

./dataGenerator.py
generate data/xsum.jsonl

./run_sweep_summarization.py
run all the settings in the experiments
outputs: outputs_sweep 把running 的 cumulative average rouge记录下来

notes：会非常罕见地出现：
Token indices sequence length is longer than the specified maximum sequence length for this model (2260 > 2048). Running this sequence through the model will result in indexing errors
This is a friendly reminder - the current text generation call will exceed the model's predefined maximum length (2048). Depending on the model, you may observe exceptions, performance degradation, or nothing at all.

collect_rouge_results.py
收集 setting + final result（最后的average rouge）
output：all_rouge_scores.csv
