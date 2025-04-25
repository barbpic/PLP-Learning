class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []
        print(f"\nCreating pet: {self.name}")

    def eat(self):
        print(f"{self.name} is eating...")
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)

    def play(self):
        if self.energy <= 0:
            print(f"{self.name} is too tired to play!")
            return
            
        print(f"{self.name} is playing...")
        self.energy = max(0, self.energy - 2)
        self.happiness = min(10, self.happiness + 2)
        self.hunger = min(10, self.hunger + 1)

    def sleep(self):
        print(f"{self.name} is sleeping...")
        self.energy = min(10, self.energy + 5)

    def train(self, trick):
        if self.energy <= 1:
            print(f"{self.name} is too tired to learn tricks!")
            return
            
        if trick in self.tricks:
            print(f"{self.name} already knows '{trick}'!")
        else:
            print(f"{self.name} is learning '{trick}'...")
            self.tricks.append(trick)
            self.energy = max(0, self.energy - 2)
            self.hunger = min(10, self.hunger + 1)

    def get_status(self):
        print(f"\n{self.name}'s current status:")
        print(f"Hunger: {self.hunger}")
        print(f"Energy: {self.energy}")
        print(f"Happiness: {self.happiness}")
        if self.tricks:
            print(f"Tricks: {self.tricks}")
        else:
            print(f"Tricks: None learned yet")

    # Bonus: Add pet type and emojis
    def set_type(self, pet_type):
        self.pet_type = pet_type
        self.emoji = self._get_emoji(pet_type)
        
    def _get_emoji(self, pet_type):
        emojis = {
            'dog': '🐶',
            'cat': '🐱',
            'bird': '🐦',
            'rabbit': '🐰',
            'fish': '🐠'
        }
        return emojis.get(pet_type.lower(), '🐾')

    def show_emoji(self):
        if hasattr(self, 'emoji'):
            print(f"\n{self.emoji} {self.name} is a {self.pet_type}!")
        else:
            print(f"\n🐾 {self.name} is ready to play!")


# Example usage
if __name__ == "__main__":
    # Create a pet
    my_pet = Pet("Felix")
    my_pet.set_type("cat")
    my_pet.show_emoji()
    
    # Perform actions
    my_pet.eat()
    my_pet.play()
    my_pet.sleep()
    
    # Train some tricks
    my_pet.train("roll over")
    my_pet.train("play dead")
    
    # Try to train when tired (edge case)
    my_pet.energy = 1
    my_pet.train("sit")  # Should fail
    
    # Show status
    my_pet.get_status()