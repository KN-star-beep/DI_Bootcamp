class Farm:
    def __init__(self, farm_name):
        # Step 2
        self.name = farm_name
        self.animals = {}

    # Step 8 (upgraded): supports both single animal and **kwargs
    def add_animal(self, animal_type=None, count=1, **kwargs):
        # Handle single animal input
        if animal_type:
            if animal_type in self.animals:
                self.animals[animal_type] += count
            else:
                self.animals[animal_type] = count

        # Handle multiple animals using kwargs
        for animal, qty in kwargs.items():
            if animal in self.animals:
                self.animals[animal] += qty
            else:
                self.animals[animal] = qty

    # Step 4
    def get_info(self):
        output = f"{self.name}'s farm\n\n"

        for animal in sorted(self.animals):
            output += f"{animal:<10} : {self.animals[animal]}\n"

        output += "\n    E-I-E-I-0!"
        return output

    # Step 6
    def get_animal_types(self):
        return sorted(self.animals.keys())

    # Step 7
    def get_short_info(self):
        animal_list = []

        for animal in self.get_animal_types():
            count = self.animals[animal]

            # pluralize if needed
            if count > 1:
                animal_list.append(animal + "s")
            else:
                animal_list.append(animal)

        # format nicely with commas and "and"
        if len(animal_list) > 1:
            animals_str = ", ".join(animal_list[:-1]) + " and " + animal_list[-1]
        else:
            animals_str = animal_list[0]

        return f"{self.name}'s farm has {animals_str}."


# ✅ Test Code
macdonald = Farm("McDonald")

# Using normal method
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)

# Using **kwargs (bonus)
macdonald.add_animal(chicken=4, duck=2)

print(macdonald.get_info())
print()
print(macdonald.get_short_info())