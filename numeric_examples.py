
#  int float
#  also bool, complex, but noone cares

i1 = 100
i2 = 2395029385209385209385209358203958203958209358209385029835
i3 = 0
i4 = -112

#  0b100 0x100 0o100

f1 = 123.456
f2 = 123.
f3 = .456
f4 = 1.23356e77

a = 35
b = 9
print(a + b, a - b)
print(a * b, a / b, a / -b, a // b, a // -b)
print(a ** b, a % b)
print()

x = 5
x *= 2    # x = x * 2
x += 10   # x = x + 10
x /= 4    # x = x / 4
print(x)

# P E (M D) (A S)

# tl;dr  use parens
result = 5 + 10 / 4 ** 8
print(result)
result = (5 + 10) / (4 ** 8)
print(result)

a = "123"
b = 456
print(int(a) + b)
print(a + str(b))







