import string
import random

# Step 2: Get all letters (uppercase and lowercase)
# string.ascii_letters contains 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
all_letters = string.ascii_letters

# Step 3: Generate a random string of length 5
random_string = ""

for _ in range(5):
    # random.choice() picks one single item from a sequence
    char = random.choice(all_letters)
    random_string += char

print(f"Your random 5-letter string is: {random_string}")