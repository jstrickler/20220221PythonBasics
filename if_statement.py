import sys

value = 92

if value >= 90 and value < 100:
    print("emu")
    print("great white shark")
elif value > 75 and value < 90:
    print("wombat")
    print("wallaby")
elif value > 50:   # else if
    print("kangaroo")
    print("quokka")
    print("platypus")
else:
    print("koala")
    print("kookaburra")

# X is False if
# X is 0
# X is None
# X is False   (builtin object)
# len(X) == 0  (if X has a length, AKA "collections")


print("All done.")

print("sys.argv: {}".format(sys.argv))

print("len(sys.argv): {}".format(len(sys.argv)))

# collections  (things that work with len() )
#  str bytes list tuple set dict

#  True False

debug = True   #  5 "yes"  87.9

color = "red" if debug else "green"
print("color: {}".format(color))

#  =  assign
# == compare

# == != > < >= <=

if value < 30 or value > 80:
    print("wahoooooooo")


if not value == 5:
    print(value)

if value != 5:
    print(value)




