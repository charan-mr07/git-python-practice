# Common String Methods
text = "  Hello World  "

print(text.strip())              # removes spaces from start/end
print(text.lower())              # converts everything to lowercase
print(text.upper())              # converts everything to uppercase
print(text.replace("World", "Python"))  # replaces a word
print(text.strip().split())      # removes spaces, splits into a list of words

name = "Charan"
print(len(name))                 # length of the string
print(name.startswith("Ch"))     # gives True/False
print(name.endswith("n"))        # gives True/False
print(name[0])                   # first character
print(name[-1])                  # last character
print(name[0:3])                 # slicing (first 3 characters)

sentence = "python is fun"
print(sentence.capitalize())     # capitalizes the first letter
print(sentence.title())          # capitalizes the first letter of every word

print("5".isdigit())              # True (checks if it's a number)
print("Charan".isalpha())         # True (checks if it's only letters)

# split() and join() — important pair
text = "apple,banana,cherry"
fruits = text.split(",")          # turns a string into a list
print(fruits)                     # ['apple', 'banana', 'cherry']

joined = "-".join(fruits)          # turns a list back into a string
print(joined)                     # apple-banana-cherry

sentence = "  Python Programming is Powerful  "

# 1. remove the spaces and print it
print(sentence.strip())

# 2. print it in all lowercase
print(sentence.lower())

# 3. replace "Powerful" with "Amazing" and print it
print(sentence.replace("Powerful", "Amazing"))

# 4. split into words and print how many words there are
words = sentence.strip().split()
print(words)
print("Number of words:", len(words))

# 5. check if the sentence starts with "Python" and print the result
print(sentence.strip().startswith("Python"))