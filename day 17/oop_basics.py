# OOP (Object-Oriented Programming) basics:
# 1.Class and an Object
# 1.1 Class = a blueprint/template
#     Object = an actual thing created from that blueprint
# Basic syntax:
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        print("Hi, I'm", self.name, "and I'm", self.age, "years old")

# Creating objects
student1 = Student("Charan", 18)
student2 = Student("Sai", 19)

student1.introduce()
student2.introduce()

#Methods(functions inside a class)
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def show_result(self):
        if self.marks >= 35:
            print(self.name, "passed with", self.marks, "marks")
        else:
            print(self.name, "failed with", self.marks, "marks")

s1 = Student("Charan", 85)
s2 = Student("Sai", 20)

s1.show_result()
s2.show_result()

# another example:
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def display_info(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year:", self.year)
        print("---")

# Creating 2 car objects
car1 = Car("Maruti Suzuki", "Swift", 2022)
car2 = Car("Hyundai", "Creta", 2023)

car1.display_info()
car2.display_info()