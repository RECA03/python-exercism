from operator import index
from uuid import RFC_4122


COLORS = [
    "black", "brown", "red", "orange", "yellow",
    "green", "blue", "violet", "grey", "white",
]
zeros = ["0","0","0","0","0","0","0","0","0"]

def label(colors):

    #numeric value of each color band
    r1 = COLORS.index(colors[0])
    r2 = COLORS.index(colors[1])
    r3 = COLORS.index(colors[2])

    #first band to str
    if r1== 0:
        p1 = ""
    else:
        p1 = str(r1)
    
    #second band to str
    p2 = str(r2)
    
    #third band equivalent 0s to str
    if r3 == 0:
        p3 = ""
    else:
        p3 = "".join(zeros[:r3])
    
    #obtaining number represented by the bands, as well as its digit length
    number = p1 + p2 + p3
    length = len(number)

    #adding ohms suffix according to the digit length
    if length < 4:
        return number + " ohms"
    elif length < 7:
        return number[:length - 3] + " kiloohms"
    elif length < 10:
        return number[:length - 6] + " megaohms"
    elif length < 13:
        return number[:length - 9] + " gigaohms"