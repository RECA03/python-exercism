COLORS = ["black","brown","red","orange","yellow",
"green","blue","violet","grey","white"]
TOLERANCES = {'grey': '±0.05%', 'violet': '±0.1%', 'blue': '±0.25%',
'green': '±0.5%', 'brown': '±1%', 'red': '±2%', 'gold': '±5%', 'silver': '±10%'}

colors = ["red", "green", "yellow", "yellow", "brown"]

#function to return value as int if it has no decimals
def float_or_int(value):
    if value % 1 == 0:
        return str(int(value))
    else:
        return str(value)

#function to add suffixes to the resistor value
def resistor_suffix_adder(value, length, tol):
    if length < 4:
        return float_or_int(value) + " ohms" + tol
    elif length < 7:
        value = value/1000
        return float_or_int(value) + " kiloohms" + tol
    elif length < 10:
        value = value/1000000
        return float_or_int(value) + " megaohms" + tol
    elif length < 13:
        value = value/1000000000
        return float_or_int(value) + " gigaohms" + tol

def resistor_label(colors):
    if len(colors) not in [1,4,5]:
        return print("invalid input")
    
    #one-band resistors
    if len(colors) == 1:
        ohms = str(COLORS.index(colors[0])) + " ohms"
        return ohms

    #for 4 band resistors
    if len(colors) == 4:
        if colors[0] == "black":
            sub_value = COLORS.index(colors[1])
        else:
            sub_value = int(str(COLORS.index(colors[0])) + str(COLORS.index(colors[1])))
        mult = COLORS.index(colors[2])
        tol = " " + TOLERANCES[colors[3]]

        value = sub_value * (10**mult)
        length = len(str(value))

        result = resistor_suffix_adder(value, length, tol)
        return result
        
    #for 5 band resistors
    if len(colors) == 5:
        if colors[0] == "black":
            sub_value = COLORS.index(colors[1]) + COLORS.index(colors[2])
        else:
            sub_value = int(str(COLORS.index(colors[0])) + str(COLORS.index(colors[1])) + str(COLORS.index(colors[2])))
        mult = COLORS.index(colors[3])
        tol = " " + TOLERANCES[colors[4]]

        value = sub_value * (10**mult)
        length = len(str(value))

        print(value)
        print(length)

        result = resistor_suffix_adder(value, length, tol)
        return result