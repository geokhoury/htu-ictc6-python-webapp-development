# List basics

# > Declaring a list
linux_distros = ['Debian', 'Ubuntu', 'Fedora',
                 'CentOS', 'OpenSUSE', 'Arch', 'Gentoo']

# > Accessing objects in a list

print(linux_distros[1])     # 'Ubuntu'
print(linux_distros[2])     # 'Fedora'

print(linux_distros)

# > Updating objects in a list

linux_distros[1] = 'Raspbian'
print(linux_distros[1])     # 'Raspbian'

linux_distros[-1] = 'Kali'
print(linux_distros[-1])     # 'Kali'

# > Print the list
print(f"The list contains {linux_distros}.")
print("The type of 'linux_distros' is '%s'." % type(linux_distros))

# > Finding the length
print("The list contains %d elements." % len(linux_distros))

# > List concatenation

other_distros = ['KDE', 'Kubuntu']
print(linux_distros + other_distros)

# > List repitition

other_distros = ['KDE', 'Kubuntu']
print(other_distros * 4)

# > Membership test
print('Fedora' in linux_distros)
print('Kubuntu' in linux_distros)
