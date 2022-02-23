#!/usr/bin/python3

spam = [
    "Spam",
    "eggs  ",
    "   spam    ",
    "     spam spam     ",
    "SPAM	",
    "       SPAM and eggs    ",
    "Spam",
    "   Spam,    spam, spam,    spam, spam, eggs, and spam      ",
]

def cleanup(s):
    return s.strip().lower()


for old_s in spam:
    new_s = cleanup(old_s)
    print(f"OLD |{old_s}|")
    print(f"NEW |{new_s}|\n")
