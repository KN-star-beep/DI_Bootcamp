import datetime

def display_current_date():
    # Step 2: Get the current date and time
    # This creates a 'datetime object' containing year, month, day, hour, etc.
    now = datetime.datetime.now()
    
    # Step 3: Display the date
    print("--- Current Date and Time ---")
    print(f"Full timestamp: {now}")
    
    # We can also pull out specific parts of the date
    print(f"Year: {now.year}")
    print(f"Month: {now.month}")
    print(f"Day: {now.day}")
    print("-----------------------------")

# Actually calling the function so it runs!
display_current_date()