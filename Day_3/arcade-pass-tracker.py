# 🕹️ Arcade Day Pass Tracker — Challenge Steps
customer_name = "john"
number_of_passes = 8
tokens_per_pass = 20
price_per_pass = 10
tokens_required_per_game = 60
total_tokens = number_of_passes*tokens_per_pass 
total_cost = number_of_passes*price_per_pass 
games_available = total_tokens//tokens_required_per_game
print("Customer name:", customer_name)
print("Number of passes:", number_of_passes)
print("Total tokens:", total_tokens)
print("Total Cost: $" + str(total_cost))
print("Games Available: " + str(games_available))

#
# 1) Create variables to store:
#    - customer name
#    - number of passes
#    - tokens per pass
#    - price per pass
#    - tokens required per game
#
# 2) Calculate:
#    - total tokens
#    - total cost
#    - games available  (use 'floor division' to get a whole number)
#
# 3) Print a summary with:
#    - customer name
#    - passes bought
#    - total tokens
#    - total cost
#    - games available