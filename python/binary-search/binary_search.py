def find(search_list, value):
    
    sorted_list = sorted(search_list)

    #prevent errors by identifying values that are out of range
    if value not in search_list:
        raise ValueError("value not in array")

    #apply binary search
    value_found = False
    left = 0
    right = len(sorted_list) - 1
    while value_found == False:
        middle_index = (left + right) // 2
        found_value = sorted_list[middle_index]

        if found_value == value:
            value_found = True
        elif found_value < value:
            left += 1
        elif found_value > value:
            right = middle_index
    
    return middle_index



            

        


    
