d1 = dict()
d2 = {'a': 5, 'm': 9, 'z': 4, 'p': 2}
print(d2.keys(), d2.values())
print(d2.items())

print(d2['a'], d2['p'])

d2['c'] = 49
d2['r'] = 8
print(d2)

d2['m'] = 31
print(d2)

d2['z'] += 10   # d2['z'] = d2['z'] + 10
print(d2)

print(d2['m'], d2['r'])
print()

airports = {
    'EWR': 'Newark',
    'YYZ': 'Toronto',
    'MCI': 'Kansas City',
    'SFO': 'San Francisco',
    'RDU': 'Raleigh-Durham',
    'SJC': 'San Jose',
    'MCO': 'Orlando',
    'YCC': 'Calgary',
    'ABQ': 'Albuquerque',
    'OAK': 'Oakland',
    'SMF': 'Sacramento',
    'YOW': 'Ottawa',
    'IAD': 'Dulles',
}

print(airports['RDU'], '\n')
# print(airports['LAX'])
for code in 'LAX', 'YCC', 'IAD', 'CMH':
    print(code, end=' ')
    if code in airports:
        print(airports[code])
    else:
        print("NOT FOUND")
print('-' * 60)


for code in 'LAX', 'YCC', 'IAD', 'CMH':
    print(code, airports.get(code, "NOT FOUND"))
print("=" * 60)

for code in 'LAX', 'YCC', 'IAD', 'CMH':
    print(code, airports.setdefault(code, 'NOT FOUND'))
print()
print(airports, '\n')

del airports['EWR']
del airports['CMH']
print(airports, '\n')

print(airports.items(), '\n')

for code, city in airports.items():
    print(code, city)
print('-' * 60)
for code, city in sorted(airports.items()):
    print(code, city)
print()

print("d2: {}".format(d2))

for letter, number in d2.items():
    print(letter, number)






