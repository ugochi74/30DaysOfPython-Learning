#!/bin/python3

if __name__ == '__main__':
    print("Type a positive number to check if it's Weird (or type 'quit' to exit).")
    
    while True:
        user_input = input("\nEnter a number: ").strip()
        
        if user_input.lower() == 'quit':
            print("Goodbye!")
            break
            
        try:
            n = int(user_input)
            
            if n <= 0:
                print("Please enter a positive number greater than 0.")
            elif n % 2 != 0:
                print("Weird")
            elif 2 <= n <= 5:
                print("Not Weird")
            elif 6 <= n <= 20:
                print("Weird")
            else:
                print("Not Weird")
                
        except ValueError:
            print("Invalid input! Please enter a whole number or 'quit'.")
