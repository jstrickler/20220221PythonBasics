#!/usr/bin/env python

import re

rx_wordsep = re.compile(r"[^a-z]+", re.I)  # <1>

s1 = '''There are 10 kinds of people in a Binary world, I hear" -- Geek talk'''

words = rx_wordsep.split(s1)  # <2>
print(words)

s2 = "Foo,   Bar,Blah   ,  Baz"

rx_splitter = re.compile(r'\s*,\s*')

print(rx_splitter.split(s2))

