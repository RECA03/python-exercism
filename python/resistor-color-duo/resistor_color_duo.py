COLOR_NAMES = [
    "black",
    "brown",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "violet",
    "grey",
    "white",
]

def value(colors):
    return int(str(COLOR_NAMES.index(colors[0])) + str(COLOR_NAMES.index(colors[1])))