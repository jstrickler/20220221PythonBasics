#!/usr/bin/python3

ctemps = [-40, 0, 37, 75, 100]

# 5-2
for celsius in ctemps:
    fahrenheit = ((9 * celsius) / 5) + 32
    print(f"{celsius} C is {fahrenheit} F")
print()

fruits = [
    '    MANGO', 'Apple', '   peach   ', 'PLUM   ', '  Apricot',
    'BaNaNa', 'Persimmon   '
]

# 5-3

clean_fruits = [f.strip().lower() for f in fruits]
print(clean_fruits)


