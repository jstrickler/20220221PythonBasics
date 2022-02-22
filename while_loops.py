
# while CONDITION:
#    statement
#    statement
#    if condition2:
#        break

i = 0
while i < 3:
    print(i)
    i += 1
print()

# while True:
#     color = input("WHAT is your favorite color? ")
#     if color == "I don't know":
#         print("The pit of death for you!")
#         break
#     else:
#         print("off you go")


while True:
    name = input("What is your name? ")
    if name == 'q':
        break
    if name == '':
        continue

    print("Welcome,", name)
