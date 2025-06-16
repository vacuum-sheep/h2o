#!/bin/bash

task=openbookqa
shots=5
model=huggyllama/llama-7b
model_arch=llama

# ratios=(0.01 0.2 0.4 0.6 0.8 1.0)
# ratios=(0.01 0.1 0.2 0.3 0.4 0.5)
ratios=(0.3 0.4)

for ratio in "${ratios[@]}"
do
  hr=$ratio
  rr=$ratio
  echo "Running with heavy_ratio=${hr}, recent_ratio=${rr}"

  python -u run_lm_eval_harness.py \
    --input-path data/summarization_data/${task}-${shots}.jsonl \
    --output-path ${task}-${shots}-${model_arch}-hr${hr}_rr${rr}.jsonl \
    --model-name ${model} \
    --model-type ${model_arch} \
    --enable_small_cache \
    --heavy_ratio ${hr} \
    --recent_ratio ${rr}
done
