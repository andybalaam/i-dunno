#!/usr/bin/env python3

from ipaddress import ip_address
from itertools import islice
import json
import sys


import i_dunno


MAX_ENCODINGS = 10


def hx(list_of_bytestr):
    return list(sorted(bytestr.hex() for bytestr in list_of_bytestr))


def enc(addr, level):
    return hx(
        islice(
            i_dunno.encode_all(addr, level=level),
            MAX_ENCODINGS
        )
    )


with open('examples.txt', 'r') as f:
    for line in f:
        case = json.loads(line)
        addr = ip_address(case["addr"])
        encs = {
            "addr": str(addr),
            "minimum": enc(addr, 'minimum'),
            "satisfactory": enc(addr, 'satisfactory'),
            "delightful": enc(addr, 'delightful'),
        }
        json.dump(encs, sys.stdout)
        sys.stdout.write("\n")
