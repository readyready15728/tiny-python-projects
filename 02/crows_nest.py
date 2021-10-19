#!/usr/bin/env python3
"""
Author : Lynn Bradshaw <readyready15728@gmail.com>
Date   : 2021-10-19
Purpose: Looking out from the ship's crow's nest
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Look out upon the seas from the vantage point of a crow's nest",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("word", metavar="word", help="A word")

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    word = args.word
    article = "an" if word[0].lower() in "aeiou" else "a"

    print(f"Ahoy, Captain, {article} {word} off the larboard bow!")


# --------------------------------------------------
if __name__ == "__main__":
    main()
