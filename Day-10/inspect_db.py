import shelve

# We must define the class structure so Python can read the binary data safely
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        return f"Player(name='{self.name}', score={self.score})"

# Open and print everything inside the database
print("--- Unlocking game_data.db ---")
with shelve.open("game_data.db") as db:
    for key in db:
        print(f"Key Found: [{key}] -> Value: {db[key]}")
