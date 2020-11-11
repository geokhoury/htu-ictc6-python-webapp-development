# The range() function

my_list = list(range(10))
print(my_list)

for i in range(5):
    # What would this print?
    print(i)

for i in range(5, 10):
    # What would this print?
    print(i)

for i in range(0, 10, 3):
    # What would this print?
    print(i)

# Using range() with lists

words = ['Mary', 'had', 'a', 'little', 'lamb']

for i in range(len(words)):
    print("Word at index %d is '%s'." % (i, words[i]))


# Evalute this
x = 0
for i in range(10):
    for j in range(-1, -10, -1):
        x += 1
        print(x)

# Evaluate this
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')
