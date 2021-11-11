#!/usr/bin/env python3
"""
Author : Lynn Bradshaw <readyready15728@gmail.com>
Date   : 2021-11-11
Purpose: n Bottles of Beer on the Wall
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='n Bottles of Beer',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n',
                        '--num',
                        metavar='number',
                        type=int,
                        default=99,
                        help='How many bottles of beer on the wall')

    args = parser.parse_args()

    if args.num < 1:
        parser.error(f'--num "{args.num}" must be greater than 0')

    return args



# --------------------------------------------------
def main():
    """Entry point for n Bottles of Beer on the Wall"""

    args = get_args()
    print('\n\n'.join(verse(i) for i in range(args.num, 0, -1)))


# --------------------------------------------------
def verse(bottle):
    """Sing a verse"""

    next_bottle = bottle - 1
    suffix_1 = '' if bottle == 1 else 's'
    suffix_2 = '' if next_bottle == 1 else 's'
    num_next = 'No more' if next_bottle == 0 else next_bottle
    return '\n'.join([
        f'{bottle} bottle{suffix_1} of beer on the wall,',
        f'{bottle} bottle{suffix_1} of beer,',
        f'Take one down, pass it around,',
        f'{num_next} bottle{suffix_2} of beer on the wall!',
    ])


# --------------------------------------------------
def test_verse():
    """Test verse"""

    last_verse = verse(1)
    assert last_verse == '\n'.join([
        '1 bottle of beer on the wall,', '1 bottle of beer,',
        'Take one down, pass it around,',
        'No more bottles of beer on the wall!'
    ])

    two_bottles = verse(2)
    assert two_bottles == '\n'.join([
        '2 bottles of beer on the wall,', '2 bottles of beer,',
        'Take one down, pass it around,', '1 bottle of beer on the wall!'
    ])


# --------------------------------------------------
if __name__ == '__main__':
    main()
