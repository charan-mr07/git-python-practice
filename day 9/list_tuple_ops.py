#1. List Methods(common ones)
fruits = ["apple", "banana", "cherry"]

fruits.append("mango")           # add at the end
fruits.insert(1, "orange")       # add at a specific position
fruits.remove("banana")          # remove by matching value
fruits.pop()                     # removes and returns the last element
fruits.pop(0)                    # remove by giving an index
fruits.sort()                    # sort in alphabetical order
fruits.reverse()                 # reverse the order
print(len(fruits))               # total count of elements
print(fruits.index("cherry"))    # shows the position of an element
fruits.clear()                   # removes all elements (empty list)

#2. List Operations (slicing, looping)
numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])       # slicing: from index 1 to 3 (4 excluded)
print(numbers[:3])        # from start to index 2
print(numbers[::-1])      # reverses the list

for num in numbers:
    print(num)

#3. Tuple Operations (remember: immutable)
coordinates = (10, 20, 30)

print(coordinates[0])           # access using index
print(coordinates[1:3])         # slicing (same as list)
print(len(coordinates))         # length
print(coordinates.count(20))    # how many times a value appears
print(coordinates.index(30))    # where the value is located

# To modify a tuple, convert it to a list first
temp_list = list(coordinates)
temp_list.append(40)
coordinates = tuple(temp_list)
print(coordinates)