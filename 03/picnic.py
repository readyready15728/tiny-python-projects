#!/usr/bin/env python3
"""
Author : Lynn Bradshaw <readyready15728@gmail.com>
Date   : 2021-10-22
Purpose: Describe picnic contributions
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Describe picnic contributions',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('items',
                        metavar='items',
                        nargs='+',
                        help='Item(s) to bring')

    parser.add_argument('-s',
                        '--sorted',
                        action='store_true',
                        help='A named string argument')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Output picnic items """

    args = get_args()
    items = args.items

    if args.sorted:
        items.sort()

    items_brought = None

    if len(items) == 1:
        items_brought = items[0]
    elif len(items) == 2:
        items_brought = f'{items[0]} and {items[1]}'
    else:
        items_brought = ', '.join(items[:-1]) + f', and {items[-1]}'

    print(f'You are bringing {items_brought}.')

# --------------------------------------------------
if __name__ == '__main__':
    main()
