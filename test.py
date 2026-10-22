print = "Hello" """ overshadowed, python interpreter will over write the built 
                in name within the current scope"""
del print
print("hello")

list = [1, 2, 3, 4] # overshadowed

clean_list = __builtins__.list((1, 2, 3, 4))
print(clean_list)

def calculate_total_sum(data):
    total = 100
    return total

print(calculate_total_sum([1, 2, 3, 4]))
print(sum([1, 2, 3, 4]))