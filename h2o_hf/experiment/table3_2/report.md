experiment:

settings difference: opt6.7b -> llama6b, T4 GPU-> two 3090 GPU

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

python3 scripts/latency_benchmark_streaming.py 

clean result:
=== Running max_gen_len = 32 ===
[THROUGHPUT] 56.04297894510555 tokens/s
=== Running max_gen_len = 512 ===
[THROUGHPUT] 84.16985925699083 tokens/s
=== Running max_gen_len = 1024 ===
[THROUGHPUT] 76.28343465624137 tokens/s

real output:

(h2o_env) kaiwen@Projgpu26:~/H2O/h2o_hf$ python3 scripts/latency_benchmark_streaming.py 


=== Running max_gen_len = 32 ===
Loading model from huggyllama/llama-7b ...
The argument `trust_remote_code` is to be used with Auto classes. It has no effect here and is ignored.
H2OKVCache-LayerWise: 4, 2000
H2OKVCache-LayerWise: 4, 2000
H2OKVCache-LayerWise: 4, 2000
H2OKVCache-LayerWise: 4, 2000
H2OKVCache-LayerWise: 4, 2000
H2OKVCache-LayerWise: 4, 2000
H2OKVCache-LayerWise: 4, 2000
H2OKVCache-LayerWise: 4, 2000
H2OKVCache-LayerWise: 4, 2000
H2OKVCache-LayerWise: 4, 2000
H2OKVCache-LayerWise: 4, 2000
H2OKVCache-LayerWise: 4, 2000
H2OKVCache-LayerWise: 4, 2000
H2OKVCache-LayerWise: 4, 2000
H2OKVCache-LayerWise: 4, 2000
H2OKVCache-LayerWise: 4, 2000
H2OKVCache-LayerWise: 4, 2000
H2OKVCache-LayerWise: 4, 2000
H2OKVCache-LayerWise: 4, 2000
H2OKVCache-LayerWise: 4, 2000
H2OKVCache-LayerWise: 4, 2000
H2OKVCache-LayerWise: 4, 2000
H2OKVCache-LayerWise: 4, 2000
H2OKVCache-LayerWise: 4, 2000
H2OKVCache-LayerWise: 4, 2000
H2OKVCache-LayerWise: 4, 2000
H2OKVCache-LayerWise: 4, 2000
H2OKVCache-LayerWise: 4, 2000
H2OKVCache-LayerWise: 4, 2000
H2OKVCache-LayerWise: 4, 2000
H2OKVCache-LayerWise: 4, 2000
H2OKVCache-LayerWise: 4, 2000
Loading checkpoint shards: 100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 2/2 [00:02<00:00,  1.15s/it]
Loading data from data/mt_bench.jsonl ...
Batch size = 4
[THROUGHPUT] 56.04297894510555


=== Running max_gen_len = 512 ===
Loading model from huggyllama/llama-7b ...
The argument `trust_remote_code` is to be used with Auto classes. It has no effect here and is ignored.
H2OKVCache-LayerWise: 4, 2000
H2OKVCache-LayerWise: 4, 2000
H2OKVCache-LayerWise: 4, 2000
H2OKVCache-LayerWise: 4, 2000
H2OKVCache-LayerWise: 4, 2000
H2OKVCache-LayerWise: 4, 2000
H2OKVCache-LayerWise: 4, 2000
H2OKVCache-LayerWise: 4, 2000
H2OKVCache-LayerWise: 4, 2000
H2OKVCache-LayerWise: 4, 2000
H2OKVCache-LayerWise: 4, 2000
H2OKVCache-LayerWise: 4, 2000
H2OKVCache-LayerWise: 4, 2000
H2OKVCache-LayerWise: 4, 2000
H2OKVCache-LayerWise: 4, 2000
H2OKVCache-LayerWise: 4, 2000
H2OKVCache-LayerWise: 4, 2000
H2OKVCache-LayerWise: 4, 2000
H2OKVCache-LayerWise: 4, 2000
H2OKVCache-LayerWise: 4, 2000
H2OKVCache-LayerWise: 4, 2000
H2OKVCache-LayerWise: 4, 2000
H2OKVCache-LayerWise: 4, 2000
H2OKVCache-LayerWise: 4, 2000
H2OKVCache-LayerWise: 4, 2000
H2OKVCache-LayerWise: 4, 2000
H2OKVCache-LayerWise: 4, 2000
H2OKVCache-LayerWise: 4, 2000
H2OKVCache-LayerWise: 4, 2000
H2OKVCache-LayerWise: 4, 2000
H2OKVCache-LayerWise: 4, 2000
H2OKVCache-LayerWise: 4, 2000
Loading checkpoint shards: 100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 2/2 [00:02<00:00,  1.16s/it]
Loading data from data/mt_bench.jsonl ...
Batch size = 4
[THROUGHPUT] 84.16985925699083


=== Running max_gen_len = 1024 ===
Loading model from huggyllama/llama-7b ...
The argument `trust_remote_code` is to be used with Auto classes. It has no effect here and is ignored.
H2OKVCache-LayerWise: 4, 2000
H2OKVCache-LayerWise: 4, 2000
H2OKVCache-LayerWise: 4, 2000
H2OKVCache-LayerWise: 4, 2000
H2OKVCache-LayerWise: 4, 2000
H2OKVCache-LayerWise: 4, 2000
H2OKVCache-LayerWise: 4, 2000
H2OKVCache-LayerWise: 4, 2000
H2OKVCache-LayerWise: 4, 2000
H2OKVCache-LayerWise: 4, 2000
H2OKVCache-LayerWise: 4, 2000
H2OKVCache-LayerWise: 4, 2000
H2OKVCache-LayerWise: 4, 2000
H2OKVCache-LayerWise: 4, 2000
H2OKVCache-LayerWise: 4, 2000
H2OKVCache-LayerWise: 4, 2000
H2OKVCache-LayerWise: 4, 2000
H2OKVCache-LayerWise: 4, 2000
H2OKVCache-LayerWise: 4, 2000
H2OKVCache-LayerWise: 4, 2000
H2OKVCache-LayerWise: 4, 2000
H2OKVCache-LayerWise: 4, 2000
H2OKVCache-LayerWise: 4, 2000
H2OKVCache-LayerWise: 4, 2000
H2OKVCache-LayerWise: 4, 2000
H2OKVCache-LayerWise: 4, 2000
H2OKVCache-LayerWise: 4, 2000
H2OKVCache-LayerWise: 4, 2000
H2OKVCache-LayerWise: 4, 2000
H2OKVCache-LayerWise: 4, 2000
H2OKVCache-LayerWise: 4, 2000
H2OKVCache-LayerWise: 4, 2000
Loading checkpoint shards: 100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 2/2 [00:02<00:00,  1.16s/it]
Loading data from data/mt_bench.jsonl ...
Batch size = 4
[THROUGHPUT] 76.28343465624137
