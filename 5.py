#!/usr/bin/env python3

import fractions
import functools

def lcm(a, b):
    return a*b // fractions.gcd(a, b)

print(functools.reduce(lcm, range(1, 21)))
