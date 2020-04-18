#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

handler = logging.FileHandler(filename="log")
handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)8s %(message)s'))
logger = logging.getLogger(__name__)
logger.addHandler(handler)

#logger.warn('hello warn')
#logger.error('hello error')
#logger.info('hello info')
#logger.debug('hello debug')


import argparse
import pysnooper # @pysnooper.snoop()
from pprint import pprint as pp
from pprint import pformat as pf

import re
import json

MATH_PATTERN = '\\\\\(.*\\\\\)'

def make_math_tag_dict(text):
    d = {}
    math_pattern_list = re.findall(MATH_PATTERN, text)
    for i, mp in enumerate(math_pattern_list):
        tag = 'HOGE{}'.format(i)
        d[tag] = mp
    return d


def math_to_tag(text, math_tag_dict):
    for tag, mp in math_tag_dict.items():
        text = text.replace(mp, tag)
    print('text') # debug
    print(text) # debug

def tag_to_math(text, math_tag_dict):
    for tag, mp in math_tag_dict.items():
        text = text.replace(tag, mp)
    print('text') # debug
    print(text) # debug


def save_math_tag_dict(filename, math_tag_dict):
    j = json.dumps(math_tag_dict, indent=4)
    with open(filename, 'w') as f:
        f.write(j)


if __name__ == '__main__':
    parser = argparse.ArgumentParser('This is hogehoge')
    parser.add_argument('filename', help='filename of tex')
    args = parser.parse_args()

    filename = args.filename
    #print('filename') # debug
    #print(filename) # debug

    with open(filename) as f:
        text = f.read()

    math_tag_dict = make_math_tag_dict(text)
    save_math_tag_dict('math_tag.json', math_tag_dict)

    math_to_tag(text, math_tag_dict)
    tag_to_math(text, math_tag_dict)






    print('\33[32m' + 'end' + '\033[0m')
