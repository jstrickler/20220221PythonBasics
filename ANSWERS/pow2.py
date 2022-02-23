#!/usr/bin/env python

raw_base = input("Enter number base: ")
base = float(raw_base)

for n in range(0, 32):
    print("{:2d} {:30.1f}".format(n, base**n))

