#!/usr/bin/env python3
"""
Author : Lynn Bradshaw <readyready15728@gmail.com>
Date   : 2021-11-19
Purpose: Make rhyming words
"""

import argparse
import io
from pydash import flatten


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Make rhyming words',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word', metavar='str', help='A word to rhyme')

    parser.add_argument('-w',
                        '--word-list',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        default='/usr/share/dict/words',
                        help='Word list to verify authenticity')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make rhyming words"""

    args = get_args()
    prefixes = list('bcdfghjklmnpqrstvwxyz') + (
        'bl br ch cl cr dr fl fr gl gr pl pr sc '
        'sh sk sl sm sn sp st sw th tr tw thw wh wr '
        'sch scr shr sph spl spr squ str thr').split()

    dict_words = read_word_list(args.word_list)

    def is_dict_word(word):
        return word.lower() in dict_words if dict_words else True

    start, rest = stemmer(args.word)

    if rest:
        print('\n'.join(sorted(filter(is_dict_word, [p + rest for p in prefixes if p != start]))))
    else:
        print(f'Cannot rhyme "{args.word}"')


# --------------------------------------------------
def stemmer(word):
    """Return leading consonants (if any), and "stem" of word"""

    word = word.lower()
    pos = list(filter(lambda v: v >= 0, map(lambda c: word.index(c) if c in word else -1, 'aeiou')))

    if pos:
        first = min(pos)
        return (word[:first], word[first:])
    else:
        return (word, '')


# --------------------------------------------------
def read_word_list(fh):
    """Read the word list file"""

    return set(flatten([line.lower().strip().split() for line in fh] if fh else []))


# --------------------------------------------------
if __name__ == '__main__':
    main()
