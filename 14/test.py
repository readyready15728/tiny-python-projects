#!/usr/bin/env python3
"""tests for rhymer.py"""

import os
import random
from subprocess import getoutput

prg = './rhymer.py'


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['', '-h', '--help']:
        out = getoutput(f'{prg} {flag}')
        assert out.lower().startswith('usage')


# --------------------------------------------------
def test_take():
    """leading consonant"""

    out = getoutput(f'{prg} take').splitlines()
    assert len(out) == 19
    assert out[0] == 'bake'
    assert out[-1] == 'wake'


# --------------------------------------------------
def test_chair():
    """consonant cluster"""

    out = getoutput(f'{prg} chair').splitlines()
    assert len(out) == 9
    assert out[1] == 'clair'
    assert out[-2] == 'pair'


# --------------------------------------------------
def test_chair_uppercase():
    """consonant cluster"""

    out = getoutput(f'{prg} CHAIR').splitlines()
    assert len(out) == 9
    assert out[1] == 'clair'
    assert out[-2] == 'pair'


# --------------------------------------------------
def test_apple():
    """leading vowel"""

    out = getoutput(f'{prg} apple').splitlines()
    assert len(out) == 3
    assert out[0] == 'dapple'
    assert out[-1] == 'snapple'


# --------------------------------------------------
def test_no_vowels():
    """no vowels"""

    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    bad = ''.join(random.sample(consonants, k=random.randint(4, 10)))
    out = getoutput(f'{prg} {bad}')
    assert out == f'Cannot rhyme "{bad}"'
