
fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

nums = [800, 80, 1000, 32, 255, 400, 5, 5000]

print(len(fruits), len(nums))
print(min(fruits), min(nums))
print(max(fruits), max(nums))
print(sorted(fruits))
print(sorted(nums))

print("nums: {}".format(nums))
r = reversed(nums)
print(r)
print("first time:")
for value in r:
    print(value)
print()

print("second time:")
for value in r:
    print(value)
print()

r = reversed(nums)
rlist = list(r)
print(rlist)
print('-' * 60)

colors = ['red', 'puce', 'ecru', 'mauve', 'yellow', 'orange'
          'pink', 'brown', 'black', 'white', 'blue']

for i, color in enumerate(colors):
    print(i, color)
print('-' * 60)

e = enumerate(colors)
print(e)
print(list(e))

i = 0
while (i < 3):
    print(i)
    i += 1
print()

for i in range(3):
    print(i)
print()

print(list(range(10)))
print(list(range(1, 12)))
print(list(range(5, 51, 5)))
print()

repeat_count = 10
for i in range(repeat_count):
    print("Python is the Best!")
print()







