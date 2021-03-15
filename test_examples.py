#!/usr/bin/env python3

from ipaddress import ip_address
from itertools import islice
import json
import sys


import i_dunno


MAX_ENCODINGS = 10


def assert_encodes_expected(case, level):
    addr = ip_address(case["addr"])
    expected = case[level]
    expected.sort()

    actual = [
        e.hex() for e in
            islice(i_dunno.encode_all(addr, level=level), MAX_ENCODINGS)
    ]
    actual.sort()
    if actual != expected:
        raise AssertionError(
            (
                'Decoding {} at level {} gave unexpected results.\n' +
                'Actual:   {}\n' +
                'Expected: {}\n'
            ).format(addr, level, actual, expected)
        )


def log(msg):
    sys.stdout.write(msg)
    sys.stdout.flush()


with open('examples.txt', 'r') as f:
    i = 0
    log('Testing')
    for line in f:
        i += 1
        if i % 1000 == 0:
            log('.')
        case = json.loads(line)
        assert_encodes_expected(case, 'minimum')
        assert_encodes_expected(case, 'satisfactory')
        assert_encodes_expected(case, 'delightful')
    log('\nTest passed.\n')

