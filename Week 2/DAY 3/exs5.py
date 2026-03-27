from datetime import datetime

def time_until_new_year():
    # Step 2: Get current date and time
    now = datetime.now()
    
    # Step 3: Create datetime object for January 1st of next year
    next_year = now.year + 1
    new_year = datetime(next_year, 1, 1)
    
    # Step 4: Calculate the time difference
    time_left = new_year - now
    
    # Step 5: Display the time difference
    print("Time left until January 1st:", time_left)

# Call the function
time_until_new_year()