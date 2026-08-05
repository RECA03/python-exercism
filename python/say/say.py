ones = {
    "0": "",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine"
}

tens = {
    "0": "",
    "1": "ten",
    "2": "twenty",
    "3": "thirty",
    "4": "forty",
    "5": "fifty",
    "6": "sixty",
    "7": "seventy",
    "8": "eighty",
    "9": "ninety"
}

eleven_through_nineteen = {
    "11": "eleven",
    "12": "twelve",
    "13": "thirteen",
    "14": "fourteen",
    "15": "fifteen",
    "16": "sixteen",
    "17": "seventeen",
    "18": "eighteen",
    "19": "nineteen"
}

hundreds = {
    "0": "",
    "1": "one hundred",
    "2": "two hundred",
    "3": "three hundred",
    "4": "four hundred",
    "5": "five hundred",
    "6": "six hundred",
    "7": "seven hundred",
    "8": "eight hundred",
    "9": "nine hundred"
}

position = {
    1: "thousand",
    2: "million",
    3: "billion"
}

def say(number):
    
    if number<0 or number>999999999999:
        raise ValueError("input out of range")
    
    number_str = str(number)
    
    triad_list = []
    processed_triad_list = []
    for i in range(len(number_str),0,-3):
        start_idx = max(0,i-3)
        triad_list.append(number_str[start_idx:i]) 
    
    for i, triad in enumerate(triad_list):

        if triad == "000":
            triad_list[i] = ""
            continue

        if len(triad) == 1:
            if triad == "0":
                triad_str = "zero"
            else:
                triad_str = ones[triad]

        if len(triad) == 2:
            if triad[0] == "1":
                triad_str = eleven_through_nineteen[triad]
            elif triad[1] != "0":
                triad_str = tens[triad[0]]+"-"+ones[triad[1]]
            else:
                triad_str = tens[triad[0]]
        
        if len(triad) == 3:
            triad_str = hundreds[triad[0]]

            if triad[2] != "0" and triad[1] != "0":
                triad_str += " " + tens[triad[1]]+"-"+ones[triad[2]]
            elif triad[1] != "0":
                triad_str += " " + tens[triad[1]]
            else:
                triad_str += ones[triad[2]]
        
        if i != 0 and triad_list[i] != "":
            triad_str += " " + position[i]
        processed_triad_list.append(triad_str)

        print(triad_str)
    
    processed_triad_list.reverse()
    
    return " ".join(processed_triad_list)