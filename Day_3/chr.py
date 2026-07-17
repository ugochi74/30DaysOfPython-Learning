#print(chr(126))

import string

def ascii_char(text):
    for char in text:
        print(f"{ord(char)}: {char}")

ascii_char(string.ascii_letters)