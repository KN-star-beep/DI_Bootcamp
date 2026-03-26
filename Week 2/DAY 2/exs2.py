class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} is barking"

    def run_speed(self):
        return (self.weight / self.age) * 10

    def fight(self, other_dog):
        my_power = self.run_speed() * self.weight
        other_power = other_dog.run_speed() * other_dog.weight

        if my_power > other_power:
            return f"{self.name} won the fight against {other_dog.name}"
        elif my_power < other_power:
            return f"{other_dog.name} won the fight against {self.name}"
        else:
            return "It's a tie!"
        
dog1 = Dog("Tusker", 4, 20)
dog2 = Dog("Koko", 5, 25)
dog3 = Dog("Tiger", 3, 18)
print(dog1.bark())            # Test bark
print(dog2.run_speed())       # Test run speed
print(dog1.fight(dog2))       # Test fight
