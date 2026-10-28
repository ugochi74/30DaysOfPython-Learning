from collections import Counter

# Analyzing page views
page_views = ["home", "about", "home", "contact", "home", "about", "home"]
view_counts = Counter(page_views)

print(view_counts)  # Counter({'home': 4, 'about': 2, 'contact': 1})
print(view_counts.most_common(2))  # [('home', 4), ('about', 2)]