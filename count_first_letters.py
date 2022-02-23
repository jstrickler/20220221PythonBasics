from pprint import pprint

counts = {}

with open('DATA/words.txt') as words_in:
    for line in words_in:
        first_letter = line[0]
        if first_letter in counts:
            counts[first_letter] += 1
            # counts[fl] = counts[fl] + 1
        else:
            counts[first_letter] = 1

pprint(counts)
