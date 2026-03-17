# 1. Create a set called my_fav_numbers
my_fav_numbers = {7, 13, 21}
print(f"Original set: {my_fav_numbers}")

# 2. Add two new numbers to the set
my_fav_numbers.add(99)
my_fav_numbers.add(50)
print(f"After adding: {my_fav_numbers}")

# 3. Remove the last number you added (or any specific number)
# Since sets are unordered, we remove a specific known value
my_fav_numbers.remove(50)
print(f"After removing: {my_fav_numbers}")

# 4. Create another set called friend_fav_numbers
friend_fav_numbers = {13, 88, 100}
print(f"Friend's set: {friend_fav_numbers}")

# 5. Concatenate (Union) to create our_fav_numbers
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
# Alternatively: our_fav_numbers = my_fav_numbers | friend_fav_numbers

print(f"Our combined set (no duplicates): {our_fav_numbers}")
