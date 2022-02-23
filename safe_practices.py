
file_path = 'DATA/wombats.txt'
with open(file_path) as wombats_in:
    for line in wombats_in:
        print(line.rstrip())

file_path = 'DATA/breakfast.txt'
with open(file_path) as breakfast_in:
    all_lines = breakfast_in.readlines() # read lines into list
    print(all_lines[25])

nums = [800, 80, 0, 50, 23, 1000, 32, 255, 400, 5, 5000]

for n in nums:
    result = 12345 / n
    print(result)


