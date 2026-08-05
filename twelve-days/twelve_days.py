gifts = ["twelve Drummers Drumming", "eleven Pipers Piping", "ten Lords-a-Leaping",
        "nine Ladies Dancing", "eight Maids-a-Milking", "seven Swans-a-Swimming",
        "six Geese-a-Laying", "five Gold Rings", "four Calling Birds",
        "three French Hens", "two Turtle Doves", "a Partridge in a Pear Tree.",]

days = {1: "first", 2: "second", 3: "third",
        4: "fourth", 5: "fifth", 6: "sixth",
        7: "seventh", 8: "eighth", 9: "ninth",
        10: "tenth", 11: "eleventh", 12: "twelfth",}

def recite(start_verse, end_verse):

    complete_recitation = []
    while start_verse <= end_verse:

        gifts_to_recite = (gifts[-start_verse:])
        if start_verse > 1:
            gifts_to_recite[-1] = "and " + gifts_to_recite[-1]
        
        complete_recitation.append(f"On the {days[start_verse]} day of Christmas my true love gave to me: {", ".join(gifts_to_recite)}")

        start_verse += 1
    
    return complete_recitation