# > Nested Functions


def outer(a, b):
    print(f"I am the outer function. I have the value a = {a} and b = {b}")
    def inner(c, d):
        print(f"I am the inner function. I have the value c = {c} and d = {d}")
        return c + d
    return inner(a, b)


result = outer(2, 4)

print(result)
# Prints 6