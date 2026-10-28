from collections import Counter

# Analyzing page views
page_views = ["about", "home", "home", "contact", "home", "about", "home", "about", "about"]
view_counts = Counter(page_views)

print(view_counts)  
print(view_counts.most_common(2))  