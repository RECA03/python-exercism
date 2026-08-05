def sum_of_multiples(limit, multiples):
    
    points_earned = set()
    for multiple in multiples:
        if multiple == 0:
            continue
        for value in range(multiple, limit, multiple): #set multiple as the step parameter
            points_earned.add(value)

    return sum(points_earned)