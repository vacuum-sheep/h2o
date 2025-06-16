task=openbookqa
shots=5
model=huggyllama/llama-7b
model_arch=llama

python -u evaluate_task_result.py \
  --result-file experiment/lm_eval_harness/openbookqa-5-llama-hr0.3_rr0.3.jsonl \
  --task-name ${task} \
  --num-fewshot ${shots} \
  --model-type ${model_arch}

# python -u evaluate_task_result.py \
#   --result-file ${task}-${shots}-${model_arch}.jsonl \
#   --task-name ${task} \
#   --num-fewshot ${shots} \
#   --model-type ${model_arch}


