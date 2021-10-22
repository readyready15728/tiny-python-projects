#!/usr/bin/env python3
"""
Author : Lynn Bradshaw <readyready15728@gmail.com>
Date   : 2021-10-22
Purpose: Jump the Five
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Jump the Five',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('input',
                        metavar='input',
                        help='Message to be encoded')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Output encoded text"""

    args = get_args()
    input_text = args.input

    jumper = {
        '1': '9',
        '2': '8',
        '3': '7',
        '4': '6',
        '5': '0',
        '6': '4',
        '7': '3',
        '8': '2',
        '9': '1',
        '0': '5'
    }

    encoded_text = ''.join([jumper[c] if c in jumper else c for c in input_text])
    print(encoded_text)


# --------------------------------------------------
if __name__ == '__main__':
    main()
