#!/usr/bin/env python3

import ipaddress
import sys

import i_dunno

print(i_dunno.encode(ipaddress.ip_address(sys.argv[1])))
