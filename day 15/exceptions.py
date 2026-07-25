''' common exception types 
ValueError, ZeroDivisionError, TypeError, IndexError, KeyError'''
# Basic syntax
try:
    num = int(input("Enter a number: "))
    print("You entered:", num)
except:
    print("That's not a valid number!") 

# Specific exceptions 
try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result:", result)
except ValueError:
    print("Please enter a valid number, not text!")
except ZeroDivisionError:
    print("Cannot divide by zero!")

# else and finaly
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Invalid input!")
else:
    print("No errors, you entered:", num)  
finally:
    print("This always runs, error occurs or not")

# 1. Divide program with ValueError and ZeroDivisionError handling
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2
    print("Result:", result)
except ValueError:
    print("Please enter valid numbers, not text!")
except ZeroDivisionError:
    print("Cannot divide by zero!")


# 2. List index program with IndexError handling
numbers = [10, 20, 30]

try:
    index = int(input("Enter an index (0-2): "))
    print("Value at that index:", numbers[index])
except ValueError:
    print("Please enter a valid number for the index!")
except IndexError:
    print("That index is out of range! List only has indices 0, 1, 2")

                   

