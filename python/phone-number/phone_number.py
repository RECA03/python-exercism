import string

class PhoneNumber:

    def __init__(self, number):
        self.number_unproc = number
        self.digits = "".join(dig for dig in self.number_unproc if dig.isdigit())
        self.area_code = self.digits[1:4] if len(self.digits) == 11 else self.digits[:3]
        self.number = self.validator()

    def validator(self):
        number_length = len(self.digits)
        number_nocountrycode = self.digits[1:] if number_length == 11 else self.digits
        area_code = number_nocountrycode[0:3]
        exchange_code = number_nocountrycode[3:6]

        print(string.punctuation)

        # no-letter chars and no punctuation chars validation 
        for char in self.number_unproc:
            if char.isalpha():
                raise ValueError("letters not permitted")
            if char in string.punctuation and char not in "() -+.":
                raise ValueError("punctuations not permitted")

        # number length validation
        if number_length < 10:
            raise ValueError("must not be fewer than 10 digits")
        elif number_length > 11:
            raise ValueError("must not be greater than 11 digits")
        
        # 11 digits validation
        print(number_length)
        print(self.digits[0])
        if number_length == 11 and self.digits[0] != "1":
            raise ValueError("11 digits must start with 1")

        # area and exchange code validation
        if area_code[0] == "0":
            raise ValueError("area code cannot start with zero")
        elif area_code[0] == "1":
            raise ValueError("area code cannot start with one")
        if exchange_code[0] == "0":
            raise ValueError("exchange code cannot start with zero")
        elif exchange_code[0] == "1":
            raise ValueError("exchange code cannot start with one")

        return self.digits[1:] if number_length == 11 else self.digits
    
    def pretty(self):
        return f"({self.number[:3]})-{self.number[3:6]}-{self.number[6:]}"