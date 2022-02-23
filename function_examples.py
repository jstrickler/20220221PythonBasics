from math import pi

MAX_TRIES = 10

# biz logic
def get_message():
    return "Hello, Apple world"


m = get_message()
print(m)

# ui logic
def display_message():
    message = get_message()
    print(message)  # user interface here...

display_message()


#               parameter
def circle_area(diameter):
    radius = diameter / 2
    return pi * (radius ** 2)

#             argument
a = circle_area(10)
b = circle_area(4.9)
c = circle_area(.75)
print(a, b, c)

def rectangle_area(length, width):
    return length * width

print(rectangle_area(5, 8))
print(rectangle_area(.5, .75))

def hello(whom="world"):  # add default parameter
    print("Hello,", whom)

hello('Mom')
hello("Las Vegas")
hello()

animal = "wombat"  # FILE (AKA GLOBAL) scope


country = "New Zealand"

def spam():
    country = "Malawi"  # LOCAL scope
    print("in spam(): animal is", animal)

spam()
# print("country is", country)
print("country:", country)












