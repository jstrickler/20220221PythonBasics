from pprint import pprint

knight_data = {}

with open('DATA/knights.txt') as knights_in:
    for raw_line in knights_in:
        line = raw_line.rstrip()
        name, title, color, quest, comment = line.split(':')
        knight_data[name] = title, color, quest, comment

pprint(knight_data)
print()

for knight_name, knight_fields in sorted(knight_data.items()):
    print(knight_fields[0], knight_name)
print()

print(knight_data['Robin'][1])
