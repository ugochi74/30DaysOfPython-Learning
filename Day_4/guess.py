#import random

#target_numbers = random.randint(1, 10)
#print("i am thinking of a number from 1 to 10 ")
#count = 0
#max_count = 4
#if target_numbers < max_count:
    #guess = int(input("Take a guess: "))
    #count += 1
   # if guess < target_numbers:
   #     print("Too low! Try Again. ")
    #elif guess > target_numbers:
      #  print("Too high! Try Again. ")
   # else:
       # print(f"You got it! Congratulations. You won at {count} attempts ")
       # break


import random

# Outer loop keeps the entire game running until the player wants to quit
while True:
    target_number = random.randint(1, 10)
    attempts = 0
    max_attempts = 3

    print("\n--- New Game ---")
    print(f"I am thinking of a number between 1 and 10. You have {max_attempts} tries!")

    # Inner loop handles the guessing mechanics for the current round
    while attempts < max_attempts:
        guess = int(input("Take a guess: "))
        attempts += 1
        
        if guess < target_number:
            print("Too low! Try again.")
        elif guess > target_number:
            print("Too high! Try again.")
        else:
            print(f"You got it! Congratulations. You won in {attempts} guesses!")
            break
    else:
        print(f"Game over! You ran out of guesses. The number was {target_number}.")

    # 1. Ask the player if they want to play another round
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    
    # 2. Break the outer loop if they type 'no' or 'n'
    if play_again not in ['yes', 'y']:
        print("Thanks for playing! Goodbye.")
        break

        