def movie_ticket_calculator():
    total_cost = 0
    print("--- Movie Ticket Cost Calculator ---")
    print("Enter 'done' when you have finished adding all family members.\n")

    while True:
        entry = input("Enter the person's age: ").lower()
        
        # Stop the loop if the user types 'done'
        if entry == 'done':
            break
            
        try:
            age = int(entry)
            
            # Apply pricing rules
            if age < 3:
                cost = 0
                print(f"Age {age}: Free")
            elif 3 <= age <= 12:
                cost = 10
                print(f"Age {age}: $10")
            else:
                cost = 15
                print(f"Age {age}: $15")
                
            total_cost += cost
            
        except ValueError:
            print("Invalid input. Please enter a number or 'done'.")

    print("-" * 30)
    print(f"Total Ticket Cost: ${total_cost}")

# To run the interactive version, uncomment the line below:
# movie_ticket_calculator()