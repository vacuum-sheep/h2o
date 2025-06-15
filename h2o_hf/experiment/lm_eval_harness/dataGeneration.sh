task=openbookqa
shots=5
model=huggyllama/llama-7b
model_arch=llama

python -u generate_task_data.py \
  --output-file ${task}-${shots}.jsonl \
  --task-name ${task} \
  --num-fewshot ${shots}
