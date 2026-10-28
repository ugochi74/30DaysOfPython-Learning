from collections import OrderedDict

od = OrderedDict()
od["a"] = 1
od["b"] = 2

print("Direct dictionary output:", od)

#  Print key-value pairs
print("Iterating through pairs:")
for key, value in od.items():
    print(f"  {key}: {value}")
