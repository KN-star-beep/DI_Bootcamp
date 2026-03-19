# Step 1: Define the function with a default value for 'country'
def describe_city(city, country="Unknown"):
    # Step 2: Print the message using an f-string
    print(f"{city} is in {country}.")

# Step 3: Call the function with different combinations
# 1. Providing both arguments
describe_city("Reykjavik", "Iceland")

# 2. Providing only the city (uses the default "Unknown")
describe_city("Paris")

# 3. Another example with both
describe_city("Tokyo", "Japan")