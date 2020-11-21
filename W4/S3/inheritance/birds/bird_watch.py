from bird import Bird
from penguin import Penguin, find_older
from parrot import Parrot


def print_bird(bird):
    Bird.who_is_this(bird)

# Create instances of the Bird class
some_bird = Bird("Some Bird", 12)
another_bird = Bird("Another Bird", 8)

# > Print the object
print(some_bird)
print(another_bird)

# > Call some methods on the Bird objects

some_bird.fly()
another_bird.eat('rice')
some_bird.dance()

# Create instances of the Parrot class

blu = Parrot("Blu", 2)
woo = Parrot("Woo", 4)

# > Call some methods on the Parrot objects

blu.fly()
woo.eat('rice')
blu.dance()
woo.dance()
blu.eat('nuts')
woo.eat('mango')

blu.celebrate_birthday()

# Create instances of the Penguin class
peggy = Penguin("Sue", 3)
zeek = Penguin("Zeek", 4)
kowalski = Penguin("Kowalski", 10)

# > Call some methods on the Penguin objects

peggy.run()
peggy.who_is_this()
peggy.fly()

peggy.find_krill()
peggy.find_krill()
peggy.find_krill()

peggy.befriend(zeek)
peggy.befriend(kowalski)
kowalski.befriend(zeek)
kowalski.befriend(peggy)

peggy.print_friends()
kowalski.print_friends()

older_penguin = find_older(peggy, zeek)
print(f"The older penguin is {older_penguin.name}.")

# > Print the objects

print(blu)              # Calls __str__() from Parrot
print(peggy)            # Calls __str__() from Bird
print(some_bird)        # Calls __str__() from Bird
print(another_bird)     # Calls __str__() from Bird
print(woo)              # Calls __str__() from Parrot


# > Function issubclass(class, classinfo)

print(f"Penguin is a Bird: {issubclass(Penguin, Bird)}")
print(f"Parrot is a Bird: {issubclass(Parrot, Bird)}")
print(f"Parrot is a Parrot: {issubclass(Parrot, Parrot)}")
print(f"Bird is a Parrot: {issubclass(Bird, Parrot)}")
print(f"Penguin is a Parrot: {issubclass(Penguin, Parrot)}")
print(f"Penguin is a Bird or Parrot or Penguin: {issubclass(Penguin, (Bird, Parrot, Penguin))}")


# > Function isinstance(object, classinfo)

print(f"blu is a Parrot: {isinstance(blu, Parrot)}")
print(f"woo is a Bird: {isinstance(woo, Bird)}")
print(f"some_bird is a Bird: {isinstance(some_bird, Bird)}")
print(f"some_bird is a Parrot: {isinstance(some_bird, Parrot)}")    # False
print(f"peggy is a Bird: {isinstance(peggy, Bird)}")
print(f"peggy is a Penguin: {isinstance(peggy, Penguin)}")
print(f"woo is a Penguin: {isinstance(woo, Penguin)}")              # False
