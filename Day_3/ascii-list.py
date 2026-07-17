import string

def ascii_list(text):
    list = []
    for char in text:
        list.append(ord(char))
    return list
result = ascii_list(string.ascii_letters)
print(result)