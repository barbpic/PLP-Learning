# Base class
class Superhero:
    def __init__(self, name, power, origin):
        self.name = name
        self.power = power
        self.origin = origin

    def introduce(self):
        return f"I am {self.name} from {self.origin}, and I have the power of {self.power}!"

    def use_power(self):
        return f"{self.name} uses {self.power}!"

# Derived class demonstrating inheritance and polymorphism
class FlyingSuperhero(Superhero):
    def __init__(self, name, power, origin, speed):
        super().__init__(name, power, origin)
        self.speed = speed

    def use_power(self):
        return f"{self.name} soars through the sky at {self.speed} km/h using {self.power}!"

# Creating objects
hero1 = Superhero("Shadow Ninja", "Invisibility", "Tokyo")
hero2 = FlyingSuperhero("Sky Blaze", "Fire Wings", "New York", 500)

# Testing the class
print(hero1.introduce())
print(hero1.use_power())

print(hero2.introduce())
print(hero2.use_power())

#ACTIVITY 2
# Demonstrating polymorphism
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

class Boat(Vehicle):
    def move(self):
        return "Sailing 🚢"

# Create a list of different vehicle instances
vehicles = [Car(), Plane(), Boat()]

# Loop through and demonstrate polymorphism
for v in vehicles:
    print(v.move())

