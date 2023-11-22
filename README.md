# Conic10K

<div align="center">
<img width="50%" src="https://github.com/whyNLP/Conic10K/assets/43395692/3e160db9-a387-4dab-a77a-d984e64d530f" />
<p>
  <!-- A dataset of conic problems
  <br>
  requires complex reasoning
  <br>
  with high-quality formal representations -->
</p>
</div>

<div align="center">
    <a href="LICENSE">
        <img alt="MIT licensed" src="https://img.shields.io/badge/license-MIT-brightgreen.svg">
    </a>
    <a href="https://paperswithcode.com/dataset/conic10k">
        <img alt="Papers With Code" src="https://tinyurl.com/yc5p8awe">
    </a>
    <a href="https://huggingface.co/datasets/WenyangHui/Conic10K">
        <img alt="Hugging Face" src="https://tinyurl.com/5n884br2">
    </a>
</div>

The official release of our project Conic10K, a large-scale dataset for closed-vocabulary math problem understanding and reasoning. The paper "[CONIC10K: A Challenging Math Problem Understanding and Reasoning Dataset](https://faculty.sist.shanghaitech.edu.cn/faculty/tukw/emnlp-f23conic.pdf)" was accepted to EMNLP 2023 Findings.

## Overview
![intro](https://github.com/whyNLP/Conic10K/assets/43395692/30b8755f-60ce-42f4-93fb-37dbfb3de983)

![example](https://github.com/whyNLP/Conic10K/assets/43395692/2f07db0e-6197-4ab7-86e2-35115f5b93dc)

## Install
To run the codes, you need to install the requirements:
```
conda create -n conic10k python=3.8
pip install torch==1.12.0+cu117 -f https://download.pytorch.org/whl/torch_stable.html
pip install -r requirements.txt
```

## Dataset
Our dataset is located in folder [`conic10k`](conic10k).

You can also get our dataset in [huggingface datasets](https://huggingface.co/datasets/WenyangHui/Conic10K).

```python
from datasets import load_dataset

dataset = load_dataset("WenyangHui/Conic10K")
train_dataset = dataset["train"]

print(train_dataset[1])
# {'text': '已知双曲线$\\frac{x^{2}}{4}-\\frac{y^{2}}{m^{2}}=1(m>0)$的一条渐近线方程是$5 x-2 y=0$，则$m$=?', 'answer_expressions': '5', 'fact_expressions': 'G: Hyperbola;m: Number;m>0;Expression(G) = (x^2/4 - y^2/m^2 = 1);Expression(OneOf(Asymptote(G))) = (5*x - 2*y = 0)', 'query_expressions': 'm', 'fact_spans': '[[[2, 49]], [[71, 74]], [[5, 49]], [[2, 49]], [[2, 69]]]', 'query_spans': '[[[71, 76]]]', 'process': '双曲线\\frac{x^{2}}{4}-\\frac{y^{2}}{m2}=1(m>0)的渐近线方程为y=\\pm\\frac{m}{2}x直线5x-2y=0的方程可化为y=\\frac{5}{2}x,所以,m=5.'}
```

Each sample in our dataset contains the following attributes.

| Attribute |  Description  |
| --- | --- | 
| text  | Question text in natural language with math formulas in latex. |
| fact_expressions  | Formal representation of the facts in the question. |
| query_expressions  | Formal representation of the queries in the question. |
| answer_expressions  | Answer to the question |
| fact_spans  | Text span corresponding to each expression in fact_expressions. |
| query_spans  | Text span corresponding to each expression in query_expressions. |
| process  | Rationale |

For more information about the annotation of this dataset, please refer to the folder [`docs`](docs) in this repo.

## Run

Run the following script to train a model. 
```bash
# Train a causal language model
sh scripts/train_clm.sh

# Train a encoder decoder model
sh scripts/train_encoder_decoder.sh
```

Run the following script to generate with a model.
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
