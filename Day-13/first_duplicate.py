

def first_duplicate(numbers):
    seen = set()
    for i in numbers:
        if i in seen:
            return i
        seen.add(i)
    return None
print(first_duplicate( [7, 2, 4, 7, 2, 7, 5, 4, 2, 2, 7]))
