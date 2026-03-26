# Base Pets class
class Pets:
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


# Base Cat class
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f"{self.name} is just walking around"


# Other Cat breeds
class Bengal(Cat):
    pass


class Chartreux(Cat):
    pass


# Step 1: Siamese class
class Siamese(Cat):
    pass


# Step 2: Create instances
cat1 = Bengal("Leo", 3)
cat2 = Chartreux("Milo", 5)
cat3 = Siamese("Luna", 2)

all_cats = [cat1, cat2, cat3]


# Step 3: Create Pets instance
sara_pets = Pets(all_cats)


# Step 4: Walk all cats
sara_pets.walk()