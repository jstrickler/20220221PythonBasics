name = "Chris Hemsworth"
city = "Melbourne"
value = 14.39839883

print(name, city)

# SEP = ' '     END = '\n'
# print(str(name) + SEP + str(city) + END)

# print"(str(name) + ' ' + str(city) + '\n')"

print("name, 'is from', city")

print(name)  # print(str(name) + '\n')
print(city)
print(value)

print()
print(name, end=" ")
print(city)

print(name, "is from", city)
print("{} is from {}".format(name, city))  # normal py3 format
print(f"{name} is from {city}")  # f-string

print("value {:.2f}".format(value))
print(f"value is {value}")
print(f"value is {value:.2f}")





