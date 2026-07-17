#print(chr(33))
import string
def ascii_int():
    for char in range(32, 127):
        print(f"{char}: {chr(char)}")
ascii_int()

