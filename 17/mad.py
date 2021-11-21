#!/usr/bin/env python3
"""
Author : Lynn Bradshaw <readyready15728@gmail.com>
Date   : 2021-11-20
Purpose: \"Mad Libs\"
"""

import argparse
import re
import sys

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='"Mad Libs"',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file', metavar='FILE',
            type=argparse.FileType('r'),
            help='Input file')

    parser.add_argument('-i',
                        '--inputs',
                        help='Inputs (for testing)',
                        metavar='str',
                        type=str,
                        nargs='*')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Render \"Mad Libs\""""

    args = get_args()
    inputs = args.inputs
    text = args.file.read().strip()
    blanks = re.findall('(<([^<>]+)>)', text)

    if not blanks:
        sys.exit(f'"{args.file.name}" has no placeholders.')

    template = 'Give me {} {}: '

    for placeholder, position in blanks:
        article = 'an' if position.lower()[0] in 'aeiou' else 'a'
        answer = inputs.pop(0) if inputs else input(template.format(article, position))
        text = re.sub(placeholder, answer, text, count=1)

    print(text)


# --------------------------------------------------
if __name__ == '__main__':
    main()
