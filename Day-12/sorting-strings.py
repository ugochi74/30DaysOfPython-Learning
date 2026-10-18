words = ["banana", "fig", "cherry", "kiwi"]

print(sorted(words, key=lambda w: len(w)))
print(sorted(words, key=lambda w: w[-1]))



students = [("Ada", 82), ("Tunde", 95), ("Ife", 70)]

print(max(students, key=lambda s: s[1]))
print(min(students, key=lambda s: s[1]))


print(sorted([3, -7, 5, -1], key=lambda n: abs(n)))
print(max(["apple", "fig", "banana"], key=lambda w: len(w)))
print(list(filter(lambda w: "a" in w, ["apple", "fig", "banana"])))


# >>> import numpy as np
# >>> array = np.array([[1, 2], [3, 4], [5, 6]])
# >>> len(array)
# 3
# >>> array.shape
# (3, 2)
# >>> len(array.shape)
# 2
