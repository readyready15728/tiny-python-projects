#!/usr/bin/env python3
"""
Author : Lynn Bradshaw <readyready15728@gmail.com>
Date   : 2021-11-11
Purpose: The Telephone Game
"""

import argparse
import os
import random
import string


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='The Telephone Game',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text', metavar='text', help='Input text or file')

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='seed',
                        type=int,
                        default=None)

    parser.add_argument('-m',
                        '--mutations',
                        help='Percent mutations',
                        metavar='mutations',
                        type=float,
                        default=0.1)

    args = parser.parse_args()

    if not 0 <= args.mutations <= 1:
        parser.error(f'--mutations "{args.mutations}" must be between 0 and 1')

    if os.path.isfile(args.text):
        args.text = open(args.text).read().strip()

    return args


# --------------------------------------------------
def main():
    """Do the telephone game"""

    args = get_args()
    text = args.text
    random.seed(args.seed)
    alphabet_and_punctuation = ''.join(sorted(string.ascii_letters + string.punctuation))
    text_length = len(text)
    num_mutations = int(round(args.mutations * text_length))
    new_text = list(text)

    for i in random.sample(range(text_length), num_mutations):
        # The call to .replace() makes sure the new letter isn't the same as
        # the old one
        new_text[i] = random.choice(alphabet_and_punctuation.replace(new_text[i], ''))

    print('You said: "{}"\nI heard: "{}"'.format(text, ''.join(new_text)))

# --------------------------------------------------
if __name__ == '__main__':
    main()
