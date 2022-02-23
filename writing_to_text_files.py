fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]


with open('my_fruits.txt', 'w') as fruits_out:
    for fruit in fruits:
        fruits_out.write(fruit + '\n')

#  'r'  read
#  'w'  write
#  'a'  append
#  'x'  eXclusive

with open('my_fruits.txt') as fruits_in:
    with open('my_pfruits.txt', 'w') as fruits_out:
        for line in fruits_in:
            if line.startswith('p'):
                fruits_out.write(line.upper())


with open('my_pfruits.txt') as pfruits_in:
    with open('pastable.py', 'a') as pastable_out:
        for line in pfruits_in:
            pastable_out.write(line)
