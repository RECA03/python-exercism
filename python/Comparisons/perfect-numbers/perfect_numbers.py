def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """

    if number > 0:
        i = 1
        aliquot_list = []

        while i < number:
                
            num_mod = number % i
            if num_mod == 0:
                aliquot_list.append(i)
            i += 1

        aliquot_sum = sum(aliquot_list)
        
        if aliquot_sum == number:
            return "perfect"
        elif aliquot_sum > number:
            return "abundant"
        elif aliquot_sum < number:
            return "deficient"

    else:
        raise ValueError("Classification is only possible for positive integers.")
    
    


