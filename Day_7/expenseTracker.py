def add_expenses(expenses, item, amount, category):
    new_expense = {"item": item, "amount": amount, "category": category}
    expenses.append(new_expense)
def show_expenses(expenses):
    for expense in expenses:
        print(f"{expense['item']} - {expense['amount']} ({expense['category']})")
def total_expenses(expenses):
    total = 0
    for expense in expenses:
        total += expense["amount"]
    return total
def filter_by_category(expenses, category):
    filtered_list = []
    for expense in expenses:
        if expense["category"] == category:
            filtered_list.append(expense)
    return filtered_list

expenses = []

while True:
    # 1. Show the menu and get the user's choice
    print("\n--- Expense Tracker Menu ---")
    choice = input("1. Add Expense\n2. Show Expenses\n3. Total Expenses\n4. Filter by Category\n5. Quit\nChoose an option (1-5): ")
    print()  # Adds a blank line for cleaner formatting
    
    # 2. Decide what to do based on the choice
    if choice == "1":
        item = input("Enter the item name: ")
        
        # --- Start of validated amount block ---
        while True:
            try:
                amount = float(input("Enter the amount: "))
                break  # Leaves the validation loop if it is a number
            except ValueError:
                print("Invalid input. Please enter a number (e.g., 1500 or 12.50).")
        # --- End of validated amount block ---
        
        category = input("Enter the category: ")
        
        add_expenses(expenses, item, amount, category)
        print(f"'{item}' successfully added!")

        
    elif choice == "2":
        print("--- All Expenses ---")
        # Call our show function to print everything line-by-line
        show_expenses(expenses)
        
    elif choice == "3":
        # Call the total function and print its returned value
        total = total_expenses(expenses)
        print(f"Total Expenses: {total}")
        
    elif choice == "4":
        target_category = input("Enter the category to filter by: ")
        # Call filter function to get a brand new list of matches
        matches = filter_by_category(expenses, target_category)
        
        print(f"\n--- Expenses in '{target_category}' ---")
        # Reuse our show function to print just the filtered list
        show_expenses(matches)
        
    elif choice == "5":
        # Break out of the infinite loop
        print("Thank you for using Expense Tracker. Goodbye!")
        break
        
    else:
        # Handle cases where the user types something invalid like "6" or "hello"
        print("Invalid choice! Please select a number between 1 and 5.")




#expenses = []
#add_expenses(expenses, "Lunch", 1500, "Food")
#add_expenses(expenses, "Bus", 300, "Transport")
#ssshow_expenses(expenses)