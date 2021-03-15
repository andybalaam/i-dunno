#!/usr/bin/env python3

from ipaddress import IPv4Address, IPv6Address
from itertools import islice
import json
from random import randrange
import sys

import i_dunno


MAX_ENCODINGS = 10


def hx(list_of_bytestr):
    return list(bytestr.hex() for bytestr in list_of_bytestr)


def enc(addr, level):
    return hx(
        islice(
            i_dunno.encode_all(addr, level=level),
            MAX_ENCODINGS
        )
    )


def print_encodings(new_addr, num):
    for i in range(num):
        addr = new_addr()
        encs = {
            "addr": str(addr),
            "minimum": enc(addr, 'minimum'),
            "satisfactory": enc(addr, 'satisfactory'),
            "delightful": enc(addr, 'delightful'),
        }
        json.dump(encs, sys.stdout)
        print()


def new_ip4():
    return IPv4Address(randrange(0, 2 ** 32))


def new_ip6():
    # Note: we only generate small addresses for now, since
    # large ones take too long because there are too many
    # possible encodings.
    return IPv6Address(randrange(0, 2 ** 128))


print_encodings(new_ip4, 10000)
print_encodings(new_ip6, 10000)
