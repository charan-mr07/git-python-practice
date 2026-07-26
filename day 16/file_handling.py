#File Handling Basics
#1. Writing to a file (write mode)
file = open("data.txt", "w")   # "w" = write mode (creates new, overwrites if it already exists)
file.write("Hello, this is my first file!\n")
file.write("Learning file handling in Python.")
file.close()   # closing the file is important, otherwise data may not save properly

#2. Reading a file (read mode)
file = open("data.txt", "r")   # "r" = read mode
content = file.read()
print(content)
file.close()

#3. with statement — better way (closes automatically)
with open("data.txt", "r") as file :
    content = file.read()
    print(content)
# the file closes automatically here, no need to manually write file.close()

#Append mode — adding new content without deleting the old
with open("data.txt", "a") as file :      # "a = append mode"
    file.write("\nThis line is added without deleting old content.")

#Reading line by line 
with open("data.txt", "r") as file :
    for line in file:
        print(line.strip())      #strip() remove the extra newline

#simple tasks
# 1. create "tasks.txt" and write 3 tasks (write mode)
with open("tasks.txt", "w") as file:
    file.write("Buy groceries\n")
    file.write("Complete Python practice\n")
    file.write("Read a book\n")

# 2. read the file and print content
with open("tasks.txt", "r") as file:
    content = file.read()
    print("Initial tasks:")
    print(content)

# 3. append a 4th task (without deleting old content)
with open("tasks.txt", "a") as file:
    file.write("Call a friend\n")

# 4. read the file again and print all tasks (line by line)
print("\nUpdated tasks:")
with open("tasks.txt", "r") as file:
    for line in file:
        print(line.strip())


