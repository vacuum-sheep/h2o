#!/bin/bash

task=openbookqa
shots=5
model_arch=llama

ratios=(0.01 0.2 0.4 0.6 0.8 1.0)

for ratio in "${ratios[@]}"
do
  # for h2o
#   hr=$(echo "$ratio / 2" | bc -l)
#   rr=$(echo "$ratio / 2" | bc -l)
#   result_file="${task}-${shots}-${model_arch}-hr${hr}_rr${rr}.jsonl"

  # for local
  result_file="experiment/lm_eval_harness/${task}-${shots}-${model_arch}-hr0_rr${ratio}.jsonl"
  
  
  echo "Evaluating ${result_file}..."
  
  python -u evaluate_task_result.py \
    --result-file "${result_file}" \
    --task-name "${task}" \
    --num-fewshot "${shots}" \
    --model-type "${model_arch}"
done
