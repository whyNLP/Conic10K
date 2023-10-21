from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
from tqdm import tqdm
import json

from data import get_dataset
from transformers import pipeline

task = 'semantic_parsing'
zero_shot = False
output_filename = 'output.json'
model_name = 'vicuna-13b'

tokenizer = AutoTokenizer.from_pretrained(model_name, local_files_only=True)
model = AutoModelForCausalLM.from_pretrained(model_name, local_files_only=True,
    torch_dtype=torch.bfloat16,
    trust_remote_code=True,
).cuda()

assert not zero_shot or task == 'semantic_parsing', 'Semantic parsing does not contain zero-shot instructions'

data = get_dataset('conic10k', zero_shot_prompt=zero_shot, task=task)['test']

def generate(text):
    input_ids = tokenizer.encode(text, return_tensors='pt').cuda()
    outputs = model.generate(input_ids, max_length=1024, do_sample=False, num_return_sequences=1, eos_token_id=tokenizer.eos_token_id)
    return tokenizer.decode(outputs[0])

if zero_shot:
    outputs = []
    for example in tqdm(data):
        outputs.append(generate(f"USER: {example['input']} ASSISTANT:"))
        with open(output_filename, 'w', encoding='utf8') as f:

            json.dump(outputs, f, ensure_ascii=False)

else:
    def generate(text):
        input_ids = tokenizer.encode(text + ' ASSISTANT:', return_tensors='pt').cuda()
        outputs = model.generate(input_ids, max_length=1024, do_sample=False, num_return_sequences=1, eos_token_id=tokenizer.eos_token_id)
        return tokenizer.decode(outputs[0])

    outputs = []
    for example in tqdm(data):
        outputs.append(generate(example['input']))
        with open(output_filename, 'w', encoding='utf8') as f:
            json.dump(outputs, f, ensure_ascii=False)