counts = {"pushed": 4, "starred": 1, "reviewed": 9, "listed": 10}

print(sorted(counts.items()))
print(sorted(counts.items(), key=lambda item: item[1]))
print(sorted(counts.items(), key=lambda item: item[1], reverse=True))