import re

class Luhn:
    
    def __init__(self, card_num):
        self.card_num  = card_num
        self.digit_list = re.findall(r"[0-9]",card_num)
        self.digit_list.reverse()

    def valid(self):

        if len(self.digit_list) <= 1: # single-digit card numbers are not valid
            return False
        if re.search(r"[^\s\d]",self.card_num): # any non-whitespace non-digit char disqualifies the card_num
            return False

        # verify wia luhn algorithm
        second_digits = [int(d)*2 if int(d)*2 <= 9 else int(d)*2-9 for d in self.digit_list[1::2]]
        non_second_digits = [int(d) for d in self.digit_list[::2]]
        return (sum(second_digits)+sum(non_second_digits))%10 == 0