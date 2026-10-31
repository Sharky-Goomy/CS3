class Vehicle:
    color = "Thermalite Gray"
    def __init__(self, name, passengers):
        self.name = name
        self.passengers = passengers
    def move(self):
        print("A vehicle colored", self.color, "with a model name of", self.name, "is moving on the road")
        print("It has", self.passengers, "passengers")

class Car(Vehicle):
    def move(self):
        print("A car colored", self.color, "with a model name of", self.name, "is moving on the road")
        print("It has", self.passengers, "passengers")

class Boat(Vehicle):
    def move(self):
        print("A boat colored", self.color, "with a model name of", self.name, "is floating on the water")
        print("It has", self.passengers, "passengers")

class Toilet(Vehicle):
    color = "Brown"
    name = "Skibidi Toilet"
    def move(self):
        print("A toilet colored", self.color, "named", self.name, "is flushing")
        print("It has", self.passengers, "passengers. You.")

car = Car("Toyota Innova", 7)
car2 = Car("BYD Seal", 5)
car2.color = "Ocean Blue"
boat = Boat("Kayak", 3)
boat.color = "Red" 
toilet = Toilet("Skibidi Toilet", 1)

vehicles = [car, car2, boat, toilet]
for vehicle in vehicles:
    vehicle.move()