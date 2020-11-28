# File IO

filename = "my_file.txt"

# opening a file for reading
my_file = open(filename, "r")   # io.TextIOWrapper

# reading lines
# print(my_file.readline())     # one line

# multiple lines
for line in my_file:
    print(f"The line says: {line}", end="")

# creating a file
another_file = open("my_new_file.txt", "w")

# writing lines
for i in range(10):
    another_file.write(f"This is line number {i+1}.\n")

# closing the file
another_file.close()

# append to a file
another_file = open("my_new_file.txt", "a+")
for i in range(2):
    another_file.write(f"This is appended line number {i+1}.\n")


# reading a binary file
my_picture = open("picture.jpg", "rb")
my_new_picture = open("my_new_picture.jpg", "wb")

for byte in my_picture:
    my_new_picture.write(byte)
