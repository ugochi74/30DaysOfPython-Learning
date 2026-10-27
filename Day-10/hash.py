inventory = {
    "apples": 50,
    "bananas": 30,
    "oranges": 25,
    "oranges": 37,
    "pineapple": 40
    }  
inventory["lemon"] = 38
inventory["apples"] = 51
del inventory["oranges"]
print(inventory) # {'apples': 50, 'bananas': 30, 'oranges': 37}
#print(inventory["apples"])
#print(inventory["pineapple"])