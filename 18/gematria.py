#!/usr/bin/env python3
"""
Author : Lynn Bradshaw <readyready15728@gmail.com>
Date   : 2021-11-20
Purpose: Gematria
"""

import argparse
import os
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Gematria',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text', metavar='text', help='Input text or file')

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().strip()

    return args


# --------------------------------------------------
def main():
    """Compute gematria"""

    args = get_args()

    for line in args.text.splitlines():
        print(' '.join(word2num(word) for word in line.split()))


# --------------------------------------------------
def word2num(word):
    """Sum the ordinal values of all the characters"""

    return str(sum(ord(c) for c in re.sub('[^A-Za-z0-9]', '', word)))


# --------------------------------------------------
if __name__ == '__main__':
    main()
