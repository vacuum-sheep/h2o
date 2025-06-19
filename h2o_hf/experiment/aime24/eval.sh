task=aime24
model=huggyllama/llama-7b
model_arch=llama

# full
python -u run_lm_eval_harness.py \
  --input-path experiment/aime24/${task}_requests.jsonl \
  --output-path experiment/aime24/${task}_full.jsonl \
  --model-name ${model} \
  --model-type ${model_arch} 

# h2o
python -u run_lm_eval_harness.py \
  --input-path experiment/aime24/${task}_requests.jsonl \
  --output-path experiment/aime24/${task}_h2o.jsonl \
  --model-name ${model} \
  --model-type ${model_arch} \
  --enable_small_cache \
  --heavy_ratio 0.1 \
  --recent_ratio 0.1
