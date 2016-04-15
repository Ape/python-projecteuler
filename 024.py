#!/usr/bin/env python3

import itertools

def nth_permutation(n):
    return next(itertools.islice(itertools.permutations(range(10)), n-1, n))

print("".join(str(x) for x in nth_permutation(1000000)))
