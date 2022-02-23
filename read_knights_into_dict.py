from pprint import pprint

FILE_PATH = 'DATA/knights.txt'

def main():  # convention to call this 'main'
    knight_data = read_data()
    pretty_print(knight_data)
    print()
    print_titles(knight_data)
    print()
    print(get_field(knight_data, 'Arthur', 1))
    print(get_field(knight_data, 'Bedevere', 3))


def read_data():
    knight_data = {}  # LOCAL variable

    with open(FILE_PATH) as knights_in:
        for raw_line in knights_in:
            line = raw_line.rstrip()
            name, title, color, quest, comment = line.split(':')
            knight_data[name] = title, color, quest, comment
    return knight_data


def pretty_print(data):
    pprint(data)


def print_titles(data):
    for knight_name, knight_fields in sorted(data.items()):
        print(knight_fields[0], knight_name)

def get_field(data, knight, field_number):
    return data[knight][field_number]

main()





