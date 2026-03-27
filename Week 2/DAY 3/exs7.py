from faker import Faker

# Step 2: Create Faker instance
fake = Faker()

# Step 3: Create empty list
users = []

# Step 4: Function to generate users
def generate_users(n):
    for _ in range(n):
        user = {
            "name": fake.name(),
            "address": fake.address(),
            "language_code": fake.language_code()
        }
        users.append(user)

# Step 5: Call function and print result
generate_users(5)

for user in users:
    print(user)