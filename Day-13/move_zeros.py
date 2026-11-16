
def move_zeros(numbers):
    non_zeros = []
    for num in numbers:
        if num != 0:
            non_zeros.append(num)
    zeros = [0] * numbers.count(0)
    return non_zeros + zeros

print(move_zeros([0, 1, 0, 3, 2, 12]))
