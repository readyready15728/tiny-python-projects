#!/usr/bin/env python3
"""
Author: Lynn Bradshaw <readyready15728@gmail.com>
Purpose: Say hello
"""

import argparse


def get_args():
    """ Get the CLI arguments """
    parser = argparse.ArgumentParser(description='Say hello')
    parser.add_argument('-n', '--name', metavar='name',
                        default='world', help='Name to greet')
    return parser.parse_args()


def main():
    """ Entry point of program """
    args = get_args()
    print(f'Hello, {args.name}!')


if __name__ == '__main__':
    main()
