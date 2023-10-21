# from torch.utils.data import Dataset, DataLoader
import numpy as np
from datasets import load_dataset

import re
import random
import json

USELESS_WORDS = [
    '已知',
    '\\'
]

TYPE_MAPPING = {
    'Ellipse': '椭圆',
    'Circle': '圆',
    'Line': '直线',
    'Point': '点',
    'Parabola': '抛物线',
    'Hyperbola': '双曲线',
    'LineSegment': '线段',
    'Ray': '射线',
    'Axis': '坐标轴',
    'Origin': '原点',
    'Curve': '曲线',
    'Triangle': '三角形',
    'Vector': '向量',
    'ConicSection': '圆锥曲线',
    'Polygon': '多边形',
    'Number': '数',
    'Real': '实数',
    'Angle': '角',
    'Unit': '单位',
    'Equation': '方程',
}


def get_dataset(
    path='conic10k',
    convert_eq=True,
    tokenize_symbols=True,
    zero_shot_prompt=False,
    task='semantic_parsing',
    encoder_decoder=False
):
    datasets = load_dataset(path)

    if zero_shot_prompt:
        datasets = datasets.map(convert_zero_shot_prompt,
                                load_from_cache_file=False)
        return datasets

    datasets = datasets.map(set_expr, load_from_cache_file=False)

    if convert_eq:
        datasets = datasets.map(convert_eq_, load_from_cache_file=False)

    if task == 'mathqa':
        datasets = datasets.filter(
            lambda x: x['answer_expressions'] is not None)
        datasets = datasets.map(lambda x: set_answer(
            x, encoder_decoder), load_from_cache_file=False)
        return datasets
    elif task == 'semantic_parsing':
        if tokenize_symbols:
            datasets = datasets.map(
                tokenize_syms, load_from_cache_file=False)
        datasets = datasets.map(lambda x: convert_instruction_tuning(
            x, encoder_decoder), load_from_cache_file=False)

    return datasets


def set_expr(example):
    # rearrange declarations to the front
    sentences = example['fact_expressions'].split(';')
    sentences = sorted([s for s in sentences if ':' in s]) + \
        sorted([s for s in sentences if ':' not in s])
    exprs = ';'.join(sentences)
    example['expr'] = exprs + ';' + \
        ';'.join(
            list(map(lambda x: x + " = ?", example['query_expressions'].split(';'))))

    return example


def set_answer(example, encoder_decoder):
    if encoder_decoder:
        return {
            'input': example['text'],
            'labels': example['answer_expressions']
        }
    else:
        return {
            'input': ("The answer of" + example['text'] + ' " is'),
            'labels': (example['answer_expressions'].strip())
        }


def convert_instruction_tuning(example, encoder_decoder):
    if encoder_decoder:
        return {
            'input': example['text'],
            'labels': example['expr']
        }
    else:
        return {
            'input': 'The translation of \"' + example['text'] + '" is',
            'labels': example['expr'].strip()
        }


def convert_eq_(example):
    # convert Eq(x, y) to x = y, need to consider nested perenthesis
    expr = example['expr']
    exprs = expr.split(';')
    new_exprs = []
    for e in exprs:
        while 'Eq(' in e:
            i = e.index('Eq(')
            j = i + 3
            cnt = 1
            tmp = e[:i]
            while cnt > 0:
                if e[j] == '(':
                    cnt += 1
                elif e[j] == ')':
                    cnt -= 1
                if cnt == 1 and e[j] == ',':
                    tmp += e[i+3:j] + '='
                    i = j + 1
                j += 1
            tmp += e[i:j-1]
            tmp += e[j:]
            e = tmp

        new_exprs.append(e)

    example['expr'] = ';'.join(new_exprs)

    return example


def convert_zero_shot_prompt(example):
    return {
        'input': '请解答下面的数学填空题\n请你一步步思考并将思考过程写在【解析】和<eoe>之间。请把你的答案写在【答案】和<eoa>之间。\n完整的题目回答格式如下：\n【解析】 ...<eoe>\n【答案】...<eoa>\n请你严格按照上述格式作答。\n题目如下:' + example['text'] + '\n【解析】',
    }


def tokenize_syms(example):
    text = example['text']
    expr = example['expr']

    # add spaces around ( ) [ ] { } < > = + - * / ^ : ; , . ? & | \ !
    text = re.sub(
        r'([\(\)\[\]\{\}\<\>\=\+\-\*\/\^\:\;\,\.\?\&\|\\\!])', r' \1 ', text)
    expr = re.sub(
        r'([\(\)\[\]\{\}\<\>\=\+\-\*\/\^\:\;\,\.\?\&\|\\\!])', r' \1 ', expr)

    # remove double spaces
    text = re.sub(r'\s+', ' ', text)
    expr = re.sub(r'\s+', ' ', expr)

    # remove space in front of numbers
    text = re.sub(r' (\d)', r'\1', text)
    expr = re.sub(r' (\d)', r'\1', expr)

    return {
        'text': text,
        'expr': expr
    }
