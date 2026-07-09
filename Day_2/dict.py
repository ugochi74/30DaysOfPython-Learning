profile = {
    "name": "odo confidence",
    "age":  20,
    "skills": ["Python", "CSS", "API", "JSON", "GO"]
}
print(profile["name"])
print(profile.get("country"))
profile["country"] = "Nigeria"
print(profile)