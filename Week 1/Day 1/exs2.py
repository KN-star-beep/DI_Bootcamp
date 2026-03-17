# Initial tuple of integers
original_tuple = (1, 2, 3)

# Attempting to directly add elements to a tuple will result in an error
try:
    original_tuple.append(4)
except AttributeError as e:
    print(f"Error: {e}") # Output: Error: 'tuple' object has no attribute 'append'

# The standard way to 'add' elements is to create a NEW tuple
# This is done using concatenation (+)
new_integers = (4, 5)
combined_tuple = original_tuple + new_integers

print(f"Original tuple: {original_tuple}")
print(f"New integers to add: {new_integers}")
print(f"Combined new tuple: {combined_tuple}")

# You can also use a variable for a single new integer,
# but remember to include a trailing comma to make it a tuple
single_integer = 6
another_combined_tuple = combined_tuple + (single_integer,) # The comma is essential

print(f"Another combined tuple: {another_combined_tuple}")
