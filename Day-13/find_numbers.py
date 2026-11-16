def find_numbers(numbers, target):
    for index, num in enumerate(numbers):
        num = numbers[index]
        if num == target:
          return index
    return -1

print(find_numbers(numbers = ([10, 25, 30, 45]), target = 30))
