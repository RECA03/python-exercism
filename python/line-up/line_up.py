def line_up(name, number):

    if number < 1 or number > 999:
        raise ValueError("number out of range")
    
    number_string = str(number)
    
    suffix_list = {"1":"st","2":"nd","3":"rd","4":"th"}

    if number_string[-2:] in ["11","12","13"]:
        number_string += suffix_list["4"]
    elif int(number_string[-1]) > 3:
        number_string += suffix_list["4"]
    elif number_string[-1] != "0":
        number_string += suffix_list[number_string[-1]]
    else:
        number_string += "th"

    return f"{name}, you are the {number_string} customer we serve today. Thank you!"