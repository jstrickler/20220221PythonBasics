fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date"]


f0 = []
for f in fruits:
    f0.append(f.upper())
print("f0: {}\n".format(f0))

#   [ thing to append for VAR in ITERABLE
f1 = [f.upper() for f in fruits]
print("f1: {}\n".format(f1))

f2 = [len(f) for f in fruits]
print("f2: {}\n".format(f2))

f3 = [f.upper() for f in fruits if f.startswith('p')]
print("f3: {}\n".format(f3))

f4 = [f for f in fruits if f.startswith('p')]
print("f4: {}\n".format(f4))

# select and or transform elements from an iterable
#  to a new list

f5 = [f.upper() for f in fruits if f.startswith('p') if len(f) > 5]
print("f5: {}\n".format(f5))

nums = [800, 80, 1000, 32, 255, 400, 5, 5000]

n1 = [n * 1000 for n in nums]
print("n1: {}\n".format(n1))

n2 = [n * 1000 for n in nums if n > 300]
print("n2: {}\n".format(n2))

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

last_names = [p[1] for p in people]
print("last_names: {}\n".format(last_names))

last_name_gen = (p[1] for p in people if p[3] > '1960')
print("last_name_gen: {}".format(last_name_gen))

for last_name in last_name_gen:
    print(last_name)
print()


























