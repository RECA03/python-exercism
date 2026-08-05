def triangle_test(sides):
    if False in [side > 0 for side in sides]:
        return False
    else:
        return (sides[0] + sides[1] >= sides[2]) and (sides[0] <= sides[1] + sides[2]) and (sides[0] + sides[2] >= sides[1])

def equilateral(sides):
    if triangle_test(sides) == True:
        return sides[0] == sides[1] == sides[2]
    else:
        return False

def isosceles(sides):
    if triangle_test(sides) == True:
        iso_sides_bool = [sides[0] == sides[1], sides[0] == sides[2], sides[1] == sides[2]]
        return sum(iso_sides_bool) >= 1
    else:
        return False

def scalene(sides):
    if triangle_test(sides) == True:
        sca_sides_bool = [sides[0] != sides[1], sides[0] != sides[2], sides[1] != sides[2]]
        return sum(sca_sides_bool) == 3
    else:
        return False