#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import json

# \\\\ で \ を表す
# \( で ( を表す
# \) で ) を表す
# . で任意の文字を表す
# * で直前の文字の0回以上の連続を表す
# .* で任意の文字列を表す
# MATH_PATTERN = '\\\\\(.*\\\\\)' # 後ろに \) があれば、できるだけ長くマッチしようとする
MATH_PATTERN = '\\\\\(.*?\\\\\)' # 最初に見つけた \) にマッチする
PACKAGE_PATTERN = '\\\\.*?\{.*?\}' # 最初に見つけた \) にマッチする

def make_math_tag_dict(text):
    d = {}
    math_pattern_list = re.findall(MATH_PATTERN, text)
    pack_pattern_list = re.findall(PACKAGE_PATTERN, text)
    pattern_list = math_pattern_list + pack_pattern_list
    for i, mp in enumerate(pattern_list):
#         print(i)
#         print(mp)
        if i < 10:
            tag = 'HOGE{}'.format(i)
        elif i < 20:
            tag = 'FUGA{}'.format(i)
        elif i < 30:
            tag = 'PIYO{}'.format(i)
        elif i < 40:
            tag = 'MOGE{}'.format(i)
        elif i < 50:
            tag = 'MUGA{}'.format(i)
        else:
            assert False
        d[tag] = mp
    return d

def load_math_tag_dict(jsonfile):
    with open(jsonfile) as f:
        math_tag_dict = json.load(f)
    return math_tag_dict

def math_to_tag(text, math_tag_dict):
    for tag, mp in math_tag_dict.items():
        text = text.replace(mp, tag)
    # print('text') # debug
    # print(text) # debug
    return text

def tag_to_math(text, math_tag_dict):
    for tag, mp in math_tag_dict.items():
        text = text.replace(tag, mp)
    # print('text') # debug
    # print(text) # debug
    return text


def save_math_tag_dict(filename, math_tag_dict):
    j = json.dumps(math_tag_dict, indent=4)
    with open(filename, 'w') as f:
        f.write(j)

def to_tag(text, jsonfile):
    math_tag_dict = make_math_tag_dict(text)
    save_math_tag_dict(jsonfile, math_tag_dict)
    return math_to_tag(text, math_tag_dict)

def to_math(text, jsonfile):
    math_tag_dict = load_math_tag_dict(jsonfile)
    return tag_to_math(text, math_tag_dict)

if __name__ == '__main__':
    import logging
    handler = logging.FileHandler(filename="log")
    handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)8s %(message)s'))
    logger = logging.getLogger(__name__)
    logger.addHandler(handler)

    # logger.warn('hello warn')
    # logger.error('hello error')
    # logger.info('hello info')
    # logger.debug('hello debug')

    import argparse

    parser = argparse.ArgumentParser('This is hogehoge')
    parser.add_argument('command', help='2tag(t) or 2math(m)', choices=['tag', 't', 'math', 'm', ])
    parser.add_argument('filename', help='filename of tex')
    parser.add_argument('--json', help='filename of math_tag json', default='math_tag.json')
    args = parser.parse_args()

    filename = args.filename
    #print('filename') # debug
    #print(filename) # debug
    jsonfile = args.json
    print('jsonfile') # debug
    print(jsonfile) # debug

    with open(filename) as f:
        text = f.read()
    if args.command in ['tag', 't']:
        to_tag(text, jsonfile)
    elif args.command in ['math', 'm']:
        to_math(text, jsonfile)

    print('\33[32m' + 'end' + '\033[0m')

