from collections import defaultdict

# Grouping items by category
products_by_category = defaultdict(list)
products = [
    ("Electronics", "Laptop"),
    ("Electronics", "Phone"),
    ("Clothing", "Shirt"),
    ("Electronics", "Tablet"),
    ("Clothing", "Pants"),
    ("food", "")
]

# Loop through each (category, product) pair and 
# if the key does not exist create an empty list for it
for category, product in products:
    products_by_category[category].append(product)

print(dict(products_by_category))
# {'Electronics': ['Laptop', 'Phone', 'Tablet'], 'Clothing': ['Shirt', 'Pants']}