
file_path = 'DATA/wombats.txt'
try:
    with open(file_path) as wombats_in:
        for line in wombats_in:
            print(line.rstrip())
except FileNotFoundError as error:
    print(error)
print()

file_path = 'DATA/breakfast.txt'
with open(file_path) as breakfast_in:
    all_lines = breakfast_in.readlines() # read lines into list
    print("len(all_lines):", len(all_lines))
    try:
        print(all_lines[25])
    except IndexError as err:
        print(err)
print()

nums = [0, 800, 80, 0, 50, 23, 1000, 32, 255, 400, 5, 5000]

for n in nums:
    try:
        result = 12345 / n
    except ZeroDivisionError as err:
        print(err)
    else:
        print(result)

print()
print("All done.")
