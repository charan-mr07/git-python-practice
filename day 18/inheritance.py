# Inheritance 
# Basic syntax:
class Animal:
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        print(self.name, "is eating")

class Dog(Animal):     # Dog inherits from Animal
    def bark(self):
        print(self.name, "is barking")

d = Dog("Tommy")
d.eat()     # method inherited from Animal
d.bark()    # Dog's own method
# class Dog(Animal): -- this says "Dog inherits from Animal"
# d.eat() -- this wasn't written in the Dog class, but it came automatically from Animal(parent)
#d.bark() -- this is amethod that only belongs to Dog

#super() — used to call the parent class's constructor
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)   # calls the parent class's __init__
        self.breed = breed
    
    def show_info(self):
        print(self.name, "is a", self.breed)

d = Dog("Tommy", "Labrador")
d.show_info()