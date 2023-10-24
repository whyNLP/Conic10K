from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
from tqdm import tqdm
import json
from transformers import pipeline
from argparse import ArgumentParser
from peft import PeftModel

from data import get_dataset

parser = ArgumentParser()
parser.add_argument('--task', type=str)
parser.add_argument('--model_name_or_path', type=str)
parser.add_argument('--output_file', type=str)
parser.add_argument('--lora_path', type=str, default='')
parser.add_argument('--dataset_path', default='conic10k', type=str)
parser.add_argument('--split', default='test', type=str, required=False)
parser.add_argument('--zero_shot', action='store_true', required=False)

if __name__ == '__main__':
    args = parser.parse_args()

    task = args.task
    zero_shot = args.zero_shot
    output_filename = args.output_file
    model_name = args.model_name_or_path
    lora_path = args.lora_path

    tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(
        model_name, 
        torch_dtype=torch.bfloat16,
        trust_remote_code=True,
    ).cuda()

    if lora_path:
        model = PeftModel.from_pretrained(
            model,
            lora_path,
            init_lora_weights=False
        )
        model.merge_and_unload()

    assert not zero_shot or task == 'semantic_parsing', 'Semantic parsing does not contain zero-shot instructions'

    data = get_dataset(args.dataset_path, zero_shot_prompt=zero_shot, task=task)[args.split]

    def generate(text):
        input_ids = tokenizer.encode(text, return_tensors='pt').cuda()
        outputs = model.generate(inputs=input_ids, max_length=1024, do_sample=False,
                                 num_return_sequences=1, eos_token_id=tokenizer.eos_token_id)
        return tokenizer.decode(outputs[0])

    outputs = []
    for example in tqdm(data):
        outputs.append(generate(example['input']))

    with open(output_filename, 'w', encoding='utf8') as f:
        json.dump(outputs, f, ensure_ascii=False)
