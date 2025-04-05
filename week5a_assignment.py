# Base class
class Superhero:
    def __init__(self, name, power, level):
        self.name = name
        self.power = power
        self.__level = level  # Private attribute

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Power: {self.power}")
        print(f"Level: {self.__level}")

    def use_power(self):
        print(f"{self.name} uses {self.power}!")

    # Getter for private attribute
    def get_level(self):
        return self.__level

    # Setter to safely update private attribute
    def set_level(self, new_level):
        if new_level >= 1:
            self.__level = new_level
        else:
            print("Level must be at least 1.")

# Subclass with added feature
class FlyingHero(Superhero):
    def __init__(self, name, power, level, flight_speed):
        super().__init__(name, power, level)
        self.flight_speed = flight_speed

    # Polymorphism - overrides use_power
    def use_power(self):
        print(f"{self.name} flies at {self.flight_speed} km/h and uses {self.power}!")

# Create objects
hero1 = Superhero("Shadow Ninja", "Invisibility", 5)
hero2 = FlyingHero("SkyBolt", "Thunder Strike", 8, 300)

# Use methods
hero1.display_info()
hero1.use_power()

print("\n---\n")

hero2.display_info()
hero2.use_power()

# Encapsulation in action
print(f"\n{hero1.name}'s current level: {hero1.get_level()}")
hero1.set_level(10)
print(f"{hero1.name}'s new level: {hero1.get_level()}")
