def find_largest(numbers):
    if numbers == []:
        return None
    target = numbers[0]
    for list in numbers:
        if list < target:
            target = list
    return target

print(find_largest([0, 3, 41, 56, 21, 76, 9]))
