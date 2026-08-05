def score(x, y):
    position = (x**2 + y**2)**(1/2)

    if position > 10:
        return 0
    elif 5 < position <= 10:
        return 1
    elif 1 < position <= 5:
        return 5
    else:
        return 10

