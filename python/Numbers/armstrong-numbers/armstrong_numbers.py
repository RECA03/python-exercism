def is_armstrong_number(number):
    digits = [int(d) for d in str(number)] # only strings can be converted to lists with list comprehension
    return sum(d ** len(digits) for d in digits) == number