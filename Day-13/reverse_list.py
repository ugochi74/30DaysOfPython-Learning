
def reverse_list(items):
    last = []
    for index in range(len(items) -1, -1, -1):
        last.append(items[index])
    return last
#input1 = ([1, 2, 3, 4])

input2 = (["a", "b", "c", "d"])
print(reverse_list(input2))