words = ["banana", "fig", "cherry", "kiwi"]

print(sorted(words, key=lambda w: len(w)))
print(sorted(words, key=lambda w: w[-1]))



students = [("Ada", 82), ("Tunde", 95), ("Ife", 70)]

print(max(students, key=lambda s: s[1]))
print(min(students, key=lambda s: s[1]))


print(sorted([3, -7, 5, -1], key=lambda n: abs(n)))
print(max(["apples", "fig", "banana"], key=lambda w: len(w)))
print(list(filter(lambda w: "a" in w, ["apple", "fig", "banana"])))