# Step 1: Define the Zoo class
class Zoo:
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = []  # empty list to store animals

    # Add animal (only if not already present)
    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    # Display all animals
    def get_animals(self):
        print("Animals in the zoo:")
        for animal in self.animals:
            print(animal)

    # Remove an animal if it exists
    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
            print(f"{animal_sold} has been sold.")
        else:
            print(f"{animal_sold} not found in the zoo.")

    # Sort and group animals alphabetically
    def sort_animals(self):
        sorted_animals = sorted(self.animals)
        grouped_animals = {}

        for animal in sorted_animals:
            first_letter = animal[0].upper()  # get first letter

            if first_letter not in grouped_animals:
                grouped_animals[first_letter] = []

            grouped_animals[first_letter].append(animal)

        return grouped_animals


# Example usage
my_zoo = Zoo("Safari Park")

my_zoo.add_animal("Lion")
my_zoo.add_animal("Zebra")
my_zoo.add_animal("Elephant")
my_zoo.add_animal("Leopard")
my_zoo.add_animal("Giraffe")
my_zoo.add_animal("Lion")  # duplicate, won't be added

my_zoo.get_animals()

my_zoo.sell_animal("Zebra")

print("\nGrouped Animals:")
print(my_zoo.sort_animals())