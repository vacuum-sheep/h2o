#!/bin/bash

task=openbookqa
shots=5
model=huggyllama/llama-7b
model_arch=llama

recent_ratios=(0.01 0.2 0.4 0.6 0.8 1.0)

for rr in "${recent_ratios[@]}"
do
  echo "Running with heavy_ratio=0, recent_ratio=${rr}"

  python -u run_lm_eval_harness.py \
    --input-path data/summarization_data/${task}-${shots}.jsonl \
    --output-path ${task}-${shots}-${model_arch}-hr0_rr${rr}.jsonl \
    --model-name ${model} \
    --model-type ${model_arch} \
    --enable_small_cache \
    --heavy_ratio 0 \
    --recent_ratio ${rr}
done
