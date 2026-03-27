from datetime import datetime

def minutes_lived(birthdate_str):
    # Step 1: Convert string to datetime object
    # Format: YYYY-MM-DD (you can change this format if you want)
    birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")
    
    # Step 2: Get current date and time
    now = datetime.now()
    
    # Step 3: Calculate time difference
    time_lived = now - birthdate
    
    # Step 4: Convert to minutes
    minutes = int(time_lived.total_seconds() / 60)
    
    # Step 5: Display result
    print(f"You have lived for approximately {minutes:,} minutes!")

# Example usage
minutes_lived("2000-05-15")