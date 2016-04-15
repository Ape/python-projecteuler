#!/usr/bin/env python3

def same_digits(a, b):
    return sorted(str(a)) == sorted(str(b))

i = 1
while not all(same_digits(i, x*i) for x in range(2, 7)):
    i += 1

print(i)
