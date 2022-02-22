list1 = list()   # new, empty, list
list2 = ['red', 'green', 'blue']
list3 = ['red', 5, 18.9, True, None, ['other', 'stuff']]

x = "foo"

list4 = []  # empty list

cities = ['Durham', 'Austin', 'Cupertino', 'Palo Alto']

print(cities[0], cities[2])

cities.insert(0, 'San Antonio')
print("cities: {}".format(cities))

cities.insert(3, 'San Diego')
print("cities: {}".format(cities))

cities.append('Dallas')
cities.append('Omaha')
print("cities: {}".format(cities))

more_cities = ['Oklahoma City', 'Las Vegas', 'Tulsa']

#             *iterable*
cities.extend(more_cities)
print("cities: {}".format(cities))
print("cities:", cities)

# cities.extend("Brooklyn")
# print("cities: {}".format(cities))

cities.insert(8, 'New York')
cities.insert(2, 'Cincinnati')
cities.append('Dallas')
print("cities: {}".format(cities))
print(len(cities))

cities[13] = 'Fort Worth'
print("cities: {}".format(cities))

del cities[1]
print("cities: {}".format(cities))

c = cities.pop()
print("c: {}".format(c))
print("cities: {}".format(cities))

c = cities.pop(3)
print("c: {}".format(c))
print("cities: {}".format(cities))

cities.remove("Tulsa")
print("cities: {}".format(cities))

#  LIST.append(obj)
#  LIST.insert(pos, obj)
#  LIST.extend(iterable)
#  del LIST[pos]
#  value = LIST.pop(pos)
#  value = LIST.pop()
#  LIST.remove(value)
print(cities[0], cities[9])
print(cities[9])
print(cities[len(cities) - 1])
print(cities[-1])

s = "spam"
print(s[-1], '\n')

print("cities: {}".format(cities))

print("cities[0:3]: {}".format(cities[0:3]))

#  LIST[start:stop]  LIST[:stop]   LIST[start:]
#  LIST[start:stop:step]
print("cities[1:4]: {}".format(cities[1:4]))

print("cities[-3:]: {}".format(cities[-3:]))
print("cities[-6:-3]: {}".format(cities[-6:-3]))

actor = 'Chris Hemsworth'
print(actor[:5])
print(actor[-5:])
print(actor[6:9])


print("cities: {}".format(cities))

for city in cities:
    #  city = first element
    #  city = second element
    #  ...
    print(city)
print()

s = "abc"
for char in s:
    print(char)
print()





























