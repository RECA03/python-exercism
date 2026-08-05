def square(number):
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    else:
        return 2 ** (number - 1)


def total():
    # simple solution // return sum(2 ** i for i in range(64))
    i = 0
    total = 0
    while i < 64:
        total += 2 ** i
        i += 1
    return total
