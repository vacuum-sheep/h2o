task=openbookqa
shots=5
model=huggyllama/llama-7b
model_arch=llama

python -u run_lm_eval_harness.py \
  --input-path data/summarization_data/${task}-${shots}.jsonl \
  --output-path ${task}-${shots}-${model_arch}.jsonl \
  --model-name ${model} \
  --model-type ${model_arch}
