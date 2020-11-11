# Famous Dinner

# You are inviting three famous people for dinner.
guests = ['nicola tesla', 'albert einstine', 'leonardo da vinci']

# Invite your guests to dinner.
name = guests[0].title()
print(f"{name}, please come to dinner.")

name = guests[1].title()
print(f"{name}, please come to dinner.")

name = guests[2].title()
print(f"{name}, please come to dinner.")

name = guests[1].title()
print(f"\nSorry, {name} can't make it to dinner.")

# TODO: Einstine can't make it on this day! Remove him and invite Socrates instead.

del(guests[1])
guests.insert(1, 'socrates')

# TODO: Print the invitations again.

name = guests[0].title()
print(f"\n{name}, please come to dinner.")

name = guests[1].title()
print(f"{name}, please come to dinner.")

name = guests[2].title()
print(f"{name}, please come to dinner.")

print("\nWe got a bigger table!")

# TODO: We got a bigger table, think of three more people and add them to the list.
# Use append() and insert() at least once

guests.insert(0, 'alan turing')
guests.insert(2, 'ken thompson')
guests.append('alan watts')

# TODO: Print the invitations again.

name = guests[0].title()
print(f"{name}, please come to dinner.")

name = guests[1].title()
print(f"{name}, please come to dinner.")

name = guests[2].title()
print(f"{name}, please come to dinner.")

name = guests[3].title()
print(f"{name}, please come to dinner.")

name = guests[4].title()
print(f"{name}, please come to dinner.")

name = guests[5].title()
print(f"{name}, please come to dinner.")


# Oh no, the table won't arrive on time!
print("\nSorry, we can only invite two people to dinner.")

# TODO: Use the following lines to remove a guest from the list, make sure you only invite two.
#       name = guests.pop()
#       print(f"Sorry, {name.title()} there's no room at the table.")

name = guests.pop()
print(f"Sorry, {name.title()} there's no room at the table.")

name = guests.pop()
print(f"Sorry, {name.title()} there's no room at the table.")

name = guests.pop()
print(f"Sorry, {name.title()} there's no room at the table.")

name = guests.pop()
print(f"Sorry, {name.title()} there's no room at the table.")

# TODO: There should be two people left. Let's invite them.
name = guests[0].title()
print(f"{name}, please come to dinner.")

name = guests[1].title()
print(f"{name}, please come to dinner.")

print("\nGood food. Good conversation.")

# Empty out your guest list.
guests.clear()
# del(guests[0])
# del(guests[0])

# Print your empty guest list
print(guests)
