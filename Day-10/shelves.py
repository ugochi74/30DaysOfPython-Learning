import shelve

with shelve.open("data.db") as db:
    db["x"] = 10
    db["x"] = 20
with shelve.open("data.db") as db:
      print(db["x"])

class Player:
    def __init__(self, name, score):
          self.name = name
          self.score = score
    def __repr__(self):
        return f"Player(name='{self.name}', score={self.score})"
with shelve.open("game_data.db") as db:
         print([*db.values()])


with shelve.open("game_data.db") as db:
         db["inventory"] = ["sword", "shield", "protection"]
         db["hero"] = Player("Arthur", 95)

with shelve.open("game_data.db") as db:
         print(db["inventory"][0])
         print(f"hero name: {db["hero"].name}, Score: {db["hero"].score}")

with shelve.open("game_data.db") as db:
      lists =  db["inventory"]
      lists.append("shelter")
      db["inventory"] = lists
# Pass writeback=True to auto-save changes, though it uses more memory
with shelve.open("game_data.db", writeback=True) as db:
    db["inventory"].append("helmet") 
    print(db["inventory"]) 

with shelve.open("game_data.db") as db:
    # 1. Check if a key exists
    if "inventory" in db:
        print("Inventory found!")
        
    # 2. Use .get() to prevent crashes on missing keys
    level = db.get("current_level", 2)  # Returns 1 if key doesn't exist
    
       
    # 3. List all saved keys
    
    # 4. Delete a key
    #if "hero" in db:
    #    del db["hero"]
        #print(db["inventory"])
with shelve.open("game_data.db") as db:
    for value in db.values():
        if isinstance(value, Player):
            print(f"Hero: {value.name} (Score: {value.score})")
        else:
            print(f"Inventory: {value}")
    
