actor = "Chris Hemsworth"

print(len(actor), type(actor))

x = actor.upper()   # call the .upper() method on the str
print(x)


print(actor.upper())
print(actor)

# immutable
print(actor.count('h'))
print(actor.count('H'))
print(actor.lower().count('h'))
print(actor.count('ris'), actor.count('sir'))

print(actor.startswith('Chris'), actor.startswith('Liam'))

print(actor)
print(actor.find('Chris'))
print(actor.find('worth'))
print(actor.find('Liam'))

s1 = "       All my exes live in Texas         "
print("|" + s1.lstrip() + "|")
print("|" + s1.rstrip() + "|")
print("|" + s1.strip() + "|")
print()


s2 = "good stuff.,,,,,,"
print(s2, s2.rstrip('.,'))

print(actor)
print(actor.replace('Chris', 'Liam'))
print(actor.replace('h', ''))

values = "   a    b              c     "
print(values.split())

record = "Seattle|WA|Fred|Jones|12345"
fields = record.split('|')
print(fields)

delim = ","
x = delim.join(fields)
x = ", ".join(fields)
print(x)

















