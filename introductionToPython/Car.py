class Car:
    def __init__(self, colour, mileage):
        self. colour = colour
        self.mileage = mileage


    def description(self):
        print(f"the {self.colour} car has {self.mileage} miles")


    def drive(self, number):
        return f"{self.mileage}"




blue = Car("Blue", 20_000)
print(blue)

print(blue.description())