# List methods

# > Declaring a list
linux_distros = ['Debian', 'Ubuntu', 'Fedora',
                 'CentOS', 'OpenSUSE', 'Arch', 'Gentoo']

# # > Appending an element
# print(f"The list contains: {linux_distros}.")
# linux_distros.append("Mint")
# linux_distros.append("Kubuntu")
# print(f"The new list contains: {linux_distros}.")

# # # >  Retrieving an element
# print(f"The list contains: {linux_distros}.")
# my_element = linux_distros.pop()            # pop the last element
# print(f"The element {my_element} was removed using pop().")
# print(f"The new list contains: {linux_distros}.")

# my_other_element = linux_distros.pop(2)     # pop the 3rd element
# print(f"The element {my_other_element} was removed using pop(i).")
# print(f"The new list contains: {linux_distros}.")

# > Inserting an element
print(f"The list contains: {linux_distros}.")
linux_distros.insert(2, "Mint")         # insert "Mint" at index 2
print(f"The new list contains: {linux_distros}.")

# # > Removing an element
# print(f"The list contains: {linux_distros}.")
# linux_distros.remove("Arch")
# print(f"The new list contains: {linux_distros}.")

# > Extending a list
debian_distros = ['Debian', 'Ubuntu', 'Mint']
print(f"The list contains: {linux_distros}.")
linux_distros.extend(debian_distros)
print(f"The new list contains: {linux_distros}.")

# > Find the index of an element
print(f"The list contains: {linux_distros}.")
print(f"The first 'Arch' is at index: {linux_distros.index('Arch')}")
print(f"The first 'Mint' is at index: {linux_distros.index('Mint')}")

# > Reverse the list
print(f"The list contains: {linux_distros}.")
linux_distros.reverse()
print(f"The new list contains: {linux_distros}.")

# > Sort the list
print(f"The list contains: {linux_distros}.")
linux_distros.sort()
print(f"The new list contains: {linux_distros}.")

# >> WWTP?
print(f"The list contains: {linux_distros}.")
linux_distros.sort()
linux_distros.reverse()
print(f"The new list contains: {linux_distros}.")

# > Clearing a list
print(f"The list contains: {linux_distros}.")
linux_distros.clear()
print(f"The new list contains: {linux_distros}.")
