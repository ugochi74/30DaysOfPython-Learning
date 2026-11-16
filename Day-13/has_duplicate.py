
def has_duplicate(numbers):
    seen = set()
    for i in numbers:
        if i in seen:
            return True
        seen.add(i)
    return False

print(has_duplicate([1, 2, 3, 2]))
print(has_duplicate([1, 2, 3, 4]))
print(has_duplicate([]))