#!/usr/bin/env python3
"""
Author : Lynn Bradshaw <readyready15728@gmail.com>
Date   : 2021-11-01
Purpose: Word Count
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        nargs='*',
                        default=[sys.stdin],
                        type=argparse.FileType('r'),
                        help='Input file(s)')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Present summary statistics of input"""

    args = get_args()

    total_lines, total_bytes, total_words = 0, 0, 0

    for fh in args.file:
        num_lines, num_words, num_bytes = 0, 0, 0

        for line in fh:
            num_lines += 1
            num_bytes += len(line.encode('utf-8')) # Properly accounts for multi-byte Unicode characters
            num_words += len(line.split())

        total_lines += num_lines
        total_bytes += num_bytes
        total_words += num_words

        print(f'{num_lines:8}{num_words:8}{num_bytes:8} {fh.name}')

    if len(args.file) > 1:
        print(f'{total_lines:8}{total_words:8}{total_bytes:8} total')


# --------------------------------------------------
if __name__ == '__main__':
    main()
