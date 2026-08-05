def primes(limit):

    if limit < 2: #in case the limit is less than 2 (smallest prime number)
        return []

    marked_numbers = set()
    unmarked_numbers = []
    for number in range(2,limit+1):
        if number in marked_numbers:
            continue

        #if the number to evaluate isn't marked, its multiples are all marked
        unmarked_numbers.append(number) 
        marked_numbers.update(range(number*2, limit+1,number))

    return unmarked_numbers