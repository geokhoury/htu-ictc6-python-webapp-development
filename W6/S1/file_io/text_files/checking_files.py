from os.path import exists
from os.path import isdir, isfile
from os.path import getsize
from os import getcwd

my_path = "south_park.txt"

# > Checking if a path exists

if exists(my_path):
    print(f"Found the path '{my_path}'.")
else:
    print(f"The path '{my_path}' was not found.")

# > Checking if a path is a file

if isfile(my_path):
    print(f"'{my_path}' is a file.")
    print(f"The file was found in '{getcwd()}'")
else:
    print(f"'{my_path}' is not a file.")

# > Checking if a path is a directory

if isdir(my_path):
    print(f"'{my_path}' is a directory.")
else:
    print(f"'{my_path}' is not a directory.")

# > Get the size of a file
south_park_num_bytes = getsize(my_path)
print(f"The size of the path '{my_path}' is {south_park_num_bytes} bytes.")