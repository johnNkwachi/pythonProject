class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def description(self):
        return f"{self.name} is {self.age} years old"


    def speek(self, sound):
        return f"{self.name} says {sound}"



buddy = Dog("Buddy", 9)
print(buddy.age)

print(buddy.description())

print(buddy.speek("woof woof"))