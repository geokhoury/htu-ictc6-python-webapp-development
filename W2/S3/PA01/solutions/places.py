# Places

# Think of at least five places in the world you’d like to visit.

# TODO: Store the locations in the list locations.
locations = ['himalaya', 'andes', 'tierra del fuego', 'labrador', 'guam']

# TODO: Print your list in its original order.
print(locations)

# TODO:
# Sort and print your list in alphabetical order wihout modifying the actual list. Read about the sorted() function.
# Show that your list is still in its original order by printing it.
print(sorted(locations))
print(locations)

# TODO:
# Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.
# Show that your list is still in its original order by printing it again.
print(sorted(locations, reverse=True))
print(locations)

# TODO: Use reverse() to change the order of your list. Print the list to show that its order has changed.
locations.reverse()
print(locations)

# TODO: Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
locations.reverse()
print(locations)

# TODO: Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
locations.sort()
print(locations)

# TODO: Use sort() to change your list so it’s stored in reverse alphabetical order. Print the list to show that its order has changed.
locations.sort(reverse=True)
# locations.reverse()
print(locations)
