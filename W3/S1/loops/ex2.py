# Flow Control - Loops

# for loops

# Iterating over a list
my_numbers_list = [2, 4, 6, 8, 10, 12]

# for number in my_numbers_list:
#     print("The number %d is even." % number)

# While loop
# i = 1
# while i <= 5:
#     print(f"i is currently: {i}")
#     i = i + 1

# > Using enumerate()

for i, v in enumerate(my_numbers_list):
    print(f"The value at index {i} is: {v}")

# Iterating over a sting

my_message = "Hello there Python web."

# my_message[0] --> H
# my_message[1] --> e
# my_message[2] --> l
# my_message[3] --> l
# my_message[4] --> o
# my_message[5] --> ,

# print(f"The following loop will iterate {len(my_message)} time.")

# for char in my_message:
#     print("%s capitalized is: %s" % (char, char.capitalize()))

# i = 0
# while i < len(my_message):
#     print("%s capitalized is: %s" %
#           (my_message[i], my_message[i].capitalize()))
#     i += 1  # i = i + 1


# > Iterating over a dictionary

favorite_songs = {
    1: {"title": "Breathe", "artist": "Pink Floyd", "tags": ["Rock", "Electric Guitar"]},
    2: {"title": "November Rain", "artist": "Guns N' Roses"},
    3: {"title": "I Want To Break Free", "artist": "Queen"},
    4: {"title": "Don't Stop Me Now", "artist": "Queen", "tags": ["Rock", "Electric Guitar"]}
}

# > Print dictionary items
for song_id in favorite_songs:
    # Get the song ID
    song = favorite_songs.get(song_id)

    # Get the song details
    title = song.get('title')
    artist = song.get('artist')
    tags = song.get('tags')

    # Print the song details
    print(f"'{title}' a great song by '{artist}'.")

    # Check if the song has tags
    if tags:
        print(f"The song has the following tags:")
        # Iterate over the tags list and print the tags
        for tag in tags:
            print(f"\t - {tag}")
    else:
        print("This song has not tags.")

# > Iterating over a netsted data structure

squares = [(1, 1), (2, 4), (3, 9), (4, 16), (5, 25), (6, 36)]

# > Iterate over the tuples
for squaret in squares:
    # What would this print?
    print(f"The square of {squaret[0]} is {squaret[1]}.")

# > Iterate over the unpacked tuples
for number, number_square in squares:
    # What would this print?
    print(f"The square of {number} is {number_square}.")

# > Infinite while loop

# while True:
#     pass  # Do nothing

# > Infinite while loop

# i = 0
# while i <= 0:
#     print("I will stop some time!")
#     i = i - 1
