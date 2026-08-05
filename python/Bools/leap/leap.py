def leap_year(year):
    leap_year = False
    if year % 100 != 0:
        if year % 4 == 0:
            leap_year = True
    else:
        if year % 400 == 0:
            leap_year = True

    return leap_year

