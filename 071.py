#!/usr/bin/env python3

from fractions import Fraction
import math

def candidates(key, max_d):
    for d in range(2, max_d):
        candidate = Fraction(math.floor(d*key), d)
        if candidate != key:
            yield candidate

print(max(candidates(Fraction(3, 7), 1000000)))
