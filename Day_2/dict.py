profile = {
    "name": "odo confidence",
    "age":  20,
    "skills": ["Python", "CSS", "API", "JSON", "GO"]
}
print(profile["name"])
print(profile.get("country"))
profile["country"] = "Nigeria"
profile.update ({"name": "confidence ugochi", "age": 19})
#print(profile.popitem())

print(profile)
