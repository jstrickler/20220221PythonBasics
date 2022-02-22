s1 = "spam\n"
print(s1)
print(s1)
print(len(s1))

#  \n is newline
#  \x is escape char
#  \n \t   \r \f \b
s2 = 'spam\n'
print(len(s2))
print(s2)
print(s2)

print("Guido's the ex-BDFL of Python")
print('Guido is the ex-"BDFL" of Python')
print("""Guido's the ex-"BDFL" of Python""")
print("Guido's the ex-\"BDFL\" of Python")

s3 = """spam\n"""
s4 = '''spam\n'''

disclaimer = """
This product is only certified
to work on Apple hardware. 

Please do not use on a PC. *PLEASE*
"""

s5 = r"spam\n"   # RAW string
print("len(s5): {}".format(len(s5)))

print("It is 25\u00B0 out")

#  \uXXXX         <= FFFF
#  \UXXXXXXXX      > FFFF










