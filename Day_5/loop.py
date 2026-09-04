for x in range(10, 20):
    if x % 15 == 0:
        continue
    print(x)
months = ["jan", "feb", "march", "apr"]
for m in (months):
    print(m)
string = "hello"
print(''.join(reversed(string)))
word = "knowledge is power indeed"
print(word.split(' ', maxsplit = 5))
characters = "   hello there  \n"
print(str.strip(characters))
word = "hello world"
print(word.count("l"))
#print(str.count(word, "e"))