import string

def ascii_sum(text):
    total_sum = 0
    for char in text:
        total_sum += ord(char)
        print(f"{char}: {ord(char)}")
    return total_sum
total_result = ascii_sum(string.ascii_letters)
print(f"Total sum: {total_result}")