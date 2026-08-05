def convert(number):
    mod3 = number % 3
    mod5 = number % 5
    mod7 = number % 7

    drops = ""

    if mod3 == 0:
        drops += "Pling"
    if mod5 == 0:
        drops += "Plang"
    if mod7 == 0:
        drops +="Plong"
    if drops == "":
        drops = str(number)

    
    return drops
