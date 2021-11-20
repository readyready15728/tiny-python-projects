#!/usr/bin/env python3
"""
Author : Lynn Bradshaw <readyready15728@gmail.com>
Date   : 2021-11-19
Purpose: Convert text to Southeastern US dialect
"""

import argparse
import os
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Convert text to Southeastern US dialect',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text', metavar='text', help='Input text or file')

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    for line in args.text.splitlines():
        print(''.join(fry(word) for word in re.split(r'(\W+)', line.rstrip())))


# --------------------------------------------------
def fry(word):
    """Drop the \"g\" from \"-ing\" words, change \"you\" to \"y'all\""""

    if word.lower() == 'you':
        # Preserves capitalization
        return word[0] + "'all"

    if word.endswith('ing'):
        if any(c.lower() in 'aeiouy' for c in word[:-3]):
            return word[:-1] + "'"

    return word


# --------------------------------------------------
if __name__ == '__main__':
    main()
