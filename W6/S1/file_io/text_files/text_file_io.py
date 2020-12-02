# File IO

filename = "my_file.txt"

# > Opening a file for reading
my_file = open(filename, "r")   # io.TextIOWrapper

# > Reading lines
# print(my_file.readline())     # one line

# > Multiple lines
for line in my_file:
    print(f"The line says: {line}", end="")

# > Creating a file
another_file = open("my_new_file.txt", "w")

# > Writing lines
for i in range(1, 11):
    another_file.write(f"I am line number {i}.\n")

# > Closing the file
another_file.close()

# > Append to a file
another_file = open("my_new_file.txt", "a+")
for i in range(1,3):
    another_file.write(f"This is appended line number {i}.\n")

for i in range(1,3):
    another_file.write(f"This is appended again.\n")

# > Closing the file
another_file.close()

# > Displaying the content of a file
with open("south_park.txt") as fp: 
    sp_buffer = fp.read()
print(sp_buffer)