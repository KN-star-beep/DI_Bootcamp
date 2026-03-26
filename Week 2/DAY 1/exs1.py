class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

# Step 1: Create three cat objects with different names and ages
cat1 = Cat("Luna", 3)
cat2 = Cat("Oliver", 7)
cat3 = Cat("Bella", 5)

# Step 2: Create a function to find the oldest cat
def find_oldest_cat(c1, c2, c3):
    # We compare the .age attribute of each object
    if c1.age > c2.age and c1.age > c3.age:
        return c1
    elif c2.age > c1.age and c2.age > c3.age:
        return c2
    else:
        return c3

# Step 3: Print the oldest cat's details
oldest = find_oldest_cat(cat1, cat2, cat3)

print(f"The oldest cat is {oldest.name}, and is {oldest.age} years old.")