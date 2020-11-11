# RGB Lookup

colours = [
    ['red', 'F00'],
    ['yellow', 'FF0'],
    ['green', '0F0'],
    ['cyan', '0FF'],
    ['blue', '00F'],
    ['magenta', 'F0F'],
]
print(f'I have learned the RGB code for {len(colours)} colours so far.')

colour = input("Please enter a colour name: ")

# DO NOT CHANGE CODE ABOVE THIS LINE

# TODO:
# Given a colour name as input from the user print the RGB code for that colour.
# The input case should be ignored, 'RED' and 'red' should both print the same code.
# The ouput should look something like this:
# >> The RGB code for 'red' is 'F00'.
#


# Change the input from the user to lowercase.
colour = colour.lower()

# Convert the list of colours to a dictionary.
colours_dict = dict(colours)

# Get the code for the colour.
colour_code = colours_dict.get(colour)

# Print the formatted output
print(f"The RGB code for '{colour}' is '{colour_code}'.")

codes = list(colours_dict.items())
