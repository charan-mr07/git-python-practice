# 1.Lambda Function
#Normal function:
def square(x):
    return x * x

print(square(5))   # 25

#Same thing with lambda:
square = lambda x: x * x
print(square(5))   # 25

#Lambda tho common use case — sorted(), filter(), map()
numbers = [5, 2, 8, 1, 9]

sorted_desc = sorted(numbers, key=lambda x: -x)
print(sorted_desc)

evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)

squared = list(map(lambda x: x * x, numbers))
print(squared)

# 2.*args--arguments(variable number)
def add_all(*args):
    total = 0
    for num in args:
        total += num
    return total

print(add_all(1, 2, 3))        # 6
print(add_all(1, 2, 3, 4, 5))  # 15

# **Kwargs
def student_info(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

student_info(name="Charan", age=18, course="ECE")