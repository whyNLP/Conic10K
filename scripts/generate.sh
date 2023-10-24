CUDA_VISIBLE_DEVICES=0 SKIP_INIT=1 python src/generate.py \
    --task semantic_parsing \
    --model_name_or_path llama-7b \
    --output_file outputs/llama-7b-lora-semantic/outputs.json \
    --lora_path outputs/llama-7b-lora-semantic \
    --split validation