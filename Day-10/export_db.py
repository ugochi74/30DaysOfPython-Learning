import json
import shelve

# 1. CRUCIAL: Python needs this blueprint to rebuild the 'hero' data!
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        return f"Player(name='{self.name}', score={self.score})"


# 2. Open and read the database safely
with shelve.open("game_data.db") as db:
    readable_data = {}
    
    for key, value in db.items():
        # Check if the value is our complex Player object
        if hasattr(value, "__dict__"):
            readable_data[key] = value.__dict__  # Converts Player object attributes to a dict
        else:
            readable_data[key] = value

# 3. Save the dictionary as a clean, viewable text file
with open("game_data_viewable.json", "w") as json_file:
    json.dump(readable_data, json_file, indent=4)

print("Success! You can now open 'game_data_viewable.json' in your text editor.")