# Step 1: Create the Dog Class
class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        # Calculate jump height as height * 2
        jump_height = self.height * 2
        print(f"{self.name} jumps {jump_height} cm high!")

# Step 2: Create Dog Objects
davids_dog = Dog("Rex", 50)
sarahs_dog = Dog("Teacup", 20)

# Step 3: Print Dog Details and Call Methods
print(f"David's dog is {davids_dog.name} and is {davids_dog.height}cm tall.")
davids_dog.bark()
davids_dog.jump()

print("-" * 20)

print(f"Sarah's dog is {sarahs_dog.name} and is {sarahs_dog.height}cm tall.")
sarahs_dog.bark()
sarahs_dog.jump()

print("-" * 20)

# Step 4: Compare Dog Sizes
if davids_dog.height > sarahs_dog.height:
    print(f"The bigger dog is {davids_dog.name}.")
elif sarahs_dog.height > davids_dog.height:
    print(f"The bigger dog is {sarahs_dog.name}.")
else:
    print("Both dogs are the same height!")