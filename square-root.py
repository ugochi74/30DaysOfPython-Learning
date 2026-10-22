cart = ["apples", "milk", "bread"]
print(cart)
size = len(cart)
mixed = ["milk", 2.5, True]
empty = []
print(size, len(mixed), len(empty), sep="\n")




import math
def foo(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return None

def bar(x):
    if x < 0:
        return None
    return math.sqrt(x)

test_inputs = [16, 25, 4, 2.25, 0, -4]

print(f"{'Input (x)':<12} | {'foo(x)':<10} | {'bar(x)':<10}")
print("-" * 40)

for x in test_inputs:
    result_foo = foo(x)
    result_bar = bar(x)
    print(f"{str(x):<12} | {str(result_foo):<10} | {str(result_bar):<10}")
