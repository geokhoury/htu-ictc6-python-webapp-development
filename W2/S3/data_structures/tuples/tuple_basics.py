# Tuple Basics

# > Packing a tuple
colors = ("Red", "Blue", "Green")
print(f"'colors' is of the type {type(colors)} and contains: {colors}.")

# > Indexing
print(colors[0])    # Red
print(colors[1])    # Blue
print(colors[-1])   # Green
print(colors[-2])   # Blue

# > Slicing
print(colors[0:1])  # ('Red')
print(colors[0:2])  # ('Red', 'Blue')

# > Unpacking a tuple
color1, color2, color3 = colors

print(color1)                   # Red
print(color1, color2, color3)   # Red Blue Green

# > Get the length
print(f"The tuple 'colors' contains {len(colors)} elements.")   # 3

# > Tuple concatenation

other_colors = ('Yellow', 'Purple')
print(colors + other_colors)

# > Tuple concatenation
my_colors = colors + other_colors

# Unpacking the tuple
a, b, c, d, e = my_colors
f, g, h, i, j = my_colors

# >> WWTP?
print(e, d, c, b, a)
print(f, g, h, i, j)

# > Tuple repition
print(my_colors * 3)

# > Membership test
my_color = 'Maroon'
print(f"Is '{my_color}' in {my_colors}? {my_color in my_colors}.")

# > min() and max()

print(f"What is the max in 'my_colors'? {max(my_colors)}")
print(f"What is the min in 'my_colors'? {min(my_colors)}")

# > Count the number of occurences
my_color = 'Yellow'
print(f"The color '{my_color}' appears {my_colors.count(my_color)} times.")

# Find the index of an element
my_color = 'Purple'
print(f"The color '{my_color}' appears at index {my_colors.index(my_color)}.")
