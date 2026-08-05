def egg_count(display_value):
    
    number = display_value
    bit_list = []
    while number > 0:
        bit_list.append(number%2)
        number //= 2
    
    eggs = bit_list.count(1)

    return eggs