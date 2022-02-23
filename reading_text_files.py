
file_path = 'DATA/mary.txt'

# PLAN A:  process each line separately (and discard)
#           file path (relative or absolute)
with open(file_path) as mary_in:  # <-- file object
    for raw_line in mary_in:   #  raw_line = mary_in.readline()
        line = raw_line.rstrip()
        print(line)
print('-' * 60)

# PLAN B: process entire file (search & replace, etc)
with open(file_path) as mary_in:
    file_contents = mary_in.read()   # read entire file into str
    print(file_contents)
    print("RAW:")
    print(repr(file_contents))
print('-' * 60)

# PLAN C: process file as list of lines; good for sorting, insert/delete, etc
with open(file_path) as mary_in:
    file_lines = mary_in.readlines()
    print(file_lines)
print('-' * 60)

with open('DATA/parrot.txt') as parrot_in:
    for raw_line in parrot_in:
        if 'bird' in raw_line:
            line = raw_line.rstrip()
            print(line)
print('-' * 60)

with open('DATA/presidents.txt') as pres_in:
    for raw_line in pres_in:
        term, last_name, first_name, dob, dod, bp, bs, ts, te, party = raw_line.rstrip().split(':')
        print(first_name, last_name)


