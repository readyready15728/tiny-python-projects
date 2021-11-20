#!/usr/bin/env python3
"""
Author : Lynn Bradshaw <readyready15728@gmail.com>
Date   : 2021-11-19
Purpose: Scramble the letters of words
"""

import argparse
import os
import random
import re


# --------------------------------------------------
def get_args():
    """Scramble the letters of words"""

    parser = argparse.ArgumentParser(
        description='Scramble the letters of words',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text', metavar='text', help='Input text or file')

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='seed',
                        type=int,
                        default=None)

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().strip()

    return args


# --------------------------------------------------
def main():
    """Scramble input text"""

    args = get_args()
    random.seed(args.seed)
    splitter = re.compile('([A-za-z](?:[A-Za-z\']*[A-za-z])?)')

    for line in args.text.splitlines():
        print(''.join(scramble(word) for word in splitter.split(line)))


# --------------------------------------------------
def scramble(word):
    """For words over 3 characters, shuffle the letters in the middle"""

    if len(word) > 3 and re.match(r'\w+', word):
        middle = list(word[1:-1])
        random.shuffle(middle)
        word = word[0] + ''.join(middle) + word[-1]

    return word


# --------------------------------------------------
if __name__ == '__main__':
    main()
