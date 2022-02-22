#!/usr/bin/env python
import sys

celsius = float(sys.argv[1])

fahrenheit = ((9 * celsius) / 5) + 32

# print("{:.1f} C is {:.1f} F".format(celsius, fahrenheit))

print(f"{celsius:.2f}\u00B0 C is {fahrenheit:.2f}\u00B0 F")
