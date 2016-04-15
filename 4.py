#!/usr/bin/env python3

import itertools

def products(limit):
    return (x*y for x,y in itertools.product(range(limit), repeat=2))

def is_palindrome(n):
    s = str(n)
    return s == s[::-1]

print(max(x for x in products(1000) if is_palindrome(x)))
