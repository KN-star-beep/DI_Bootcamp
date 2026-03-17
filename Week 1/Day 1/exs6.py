while True:
    name = "alex nganga kamau"

    # Check if the name contains any digits
    has_digit = False
    for char in name:
        if char.isdigit():
            has_digit = True
            break
    
    # Check if the name is at least 3 letters long
    is_long_enough = len(name) >= 3

    if has_digit or not is_long_enough:
        print("Invalid name. Name cannot contain digits and must be at least 3 letters long. Please try again.")
    else:
        print("Thank you")
        break
