events = [
    {"repo": "expense-tracker", "pushes": 2},
    {"repo": "campusflow", "pushes": 9},
    {"repo": "algorithms", "pushes": 1},
]

print(sorted(events, key=lambda e: e["pushes"]))



# filter and map
nums = [1, 2, 3, 4, 5, 6]

print(list(filter(lambda n: n % 2 == 0, nums)))
print(list(map(lambda n: n * 10, nums)))