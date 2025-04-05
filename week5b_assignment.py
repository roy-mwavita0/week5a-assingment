# Base class
class Vehicle:
    def move(self):
        print("The vehicle is moving.")

# Subclasses with their own versions of move()
class Car(Vehicle):
    def move(self):
        print("Driving")

class Plane(Vehicle):
    def move(self):
        print("Flying")

class Boat(Vehicle):
    def move(self):
        print("Sailing")

class Bicycle(Vehicle):
    def move(self):
        print("Pedaling")

# Create a list of vehicles
vehicles = [Car(), Plane(), Boat(), Bicycle()]

# Loop through and call move() – Polymorphism in action!
for v in vehicles:
    v.move()
