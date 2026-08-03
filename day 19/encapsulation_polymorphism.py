''' 1. Encapsulation — protecting data
Encapsulation means protecting the data inside an object from direct access,
, allowing it to be accessed/modified only in a controlled way.'''
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # using "__" prefix makes it a private variable
    
    def deposit(self, amount):
        self.__balance += amount
        print("Deposited. New balance:", self.__balance)
    
    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance!")
        else:
            self.__balance -= amount
            print("Withdrawn. New balance:", self.__balance)
    
    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
account.withdraw(200)

print(account.get_balance())   # correct way, accessed through a method
# print(account.__balance)     # this gives an ERROR, direct access isn't allowed

'''2. Polymorphism — "many forms" — same method name, different behavior in different classes
python'''
class Dog:
    def sound(self):
        print("Dog says Woof")

class Cat:
    def sound(self):
        print("Cat says Meow")

class Cow:
    def sound(self):
        print("Cow says Moo")

animals = [Dog(), Cat(), Cow()]

for animal in animals:
    animal.sound()   # same method name, but different output for each class
