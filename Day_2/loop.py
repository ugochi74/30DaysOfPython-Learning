profile = {
    "name": "odo confidence",
    "age":  20,
    "skills": ["Python", "CSS", "API", "JSON", "GO"]
}
print(profile["name"])
print(profile.get("country"))
profile["country"] = "Nigeria"
print(profile)

skills = ["JSON", "API", "Python", "Go"]
print(skills[0])
print(skills[-1])
skills.append("CSS")
print(skills)

skills = ["JSON", "API", "Python", "Go"]
for skill in skills:
    print(f"i am learning {skill}")
for key in profile:
    print(f"{key}: {profile[key]}")
    #print(key, profile[key])


