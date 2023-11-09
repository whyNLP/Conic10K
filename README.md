# Conic10K
This is the official release of our EMNLP 2023 paper, [Conic10K: A large-scale dataset for closed-vocabulary math problem understanding](link).

## Install
To run the codes, you need to install the requirements:
```
conda create -n conic10k python=3.8
pip install torch==1.12.0+cu117 -f https://download.pytorch.org/whl/torch_stable.html
pip install -r requirements.txt
```

## Dataset
Our dataset is located in [`conic10k`](conic10k).

You can also get our dataset in huggingface datasets.

```python
from datasets import load_dataset

dataset = load_dataset("WenyangHui/Conic10K")
```

Each sample in our dataset contain the following attributes.

| Attribute |  Description  |
| --- | --- | 
| text  | Question text in natural language with math formulas in latex. |
| fact_expressions  | Formal represention of the facts in the question. |
| query_expressions  | Formal represention of the queries in the question. |
| answer_expressions  | Answer to the question |
| fact_spans  | Text span corresponding to each expression in fact_expressions. |
| query_spans  | Text span corresponding to each expression in query_expressions. |
| process  | Rationale |


## Run

Run the following script to train a model. 
```bash
# Train a causal language model
sh scripts/train_clm.sh

# Train a encoder decoder model
sh scripts/train_encoder_decoder.sh
```

Run he following script to generate with a model.
```bash
python src/generate.py \
    --task semantic_parsing \
    --model_name_or_path llama-7b \
    --output_file outputs/semantic_parsing_llama_7b_lora.json \
    --lora_path llama-7b-semantic-parsing-lora
```

Run the following script to automatically evaluate the generation results in semantic parsing.
```bash
python src/semantic_evaluate.py \
    --prediction_file outputs/semantic_parsing_llama_7b_lora.json \
    --split test \
    --report_file outputs/semantic_parsing_llama_7b_lora_report.json
```

## License

This project is [MIT licensed](LICENSE).
