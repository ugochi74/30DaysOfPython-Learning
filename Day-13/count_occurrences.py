
def count_occurrences(numbers, target):
    count = 0
    for value in numbers:
       if  value == target:
        count += 1
    return count

print(count_occurrences(numbers = ([1, 4, 7]), target = 10))
