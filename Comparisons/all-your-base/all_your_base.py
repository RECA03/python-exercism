from multiprocessing import Value

def rebase(input_base, digits, output_base):
    #Raising exceptions
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    for d in digits:
        if d < 0 or d >= input_base:
            raise ValueError("all digits must satisfy 0 <= d < input base")
    
    #decodging the number
    number = sum([d*input_base**(len(digits)-1-i) for i, d in enumerate(digits)])

    #converting it to output base
    output_digits = []
    
    #if number is 0, return [0]
    if number == 0:
        return [0]

    while number > 0:
        output_digits.append(number % output_base)
        number //= output_base
    return output_digits[::-1]