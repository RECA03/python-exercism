def primes():

    prime_list =[]
    candidate = 2 # first prime is 2
    prime_counter = 0 # to keep track of what nth prime the generators is at

    while True: # generate as many primes needed
        is_prime = True
        for p in prime_list:
            if p*p > candidate: # possible dividends can only be as big as the candidate's square root
                break
            if candidate%p == 0: # candidates that can be divided by another prime cannot be primes
                is_prime = False
                break

        if is_prime:
            prime_counter += 1
            prime_list.append(candidate)
            yield(candidate, prime_counter)
        
        candidate += 1 if candidate == 2 else 2 # 2 is the only prime even number, only odds have to be checked after it

def prime(number):

    if number < 1:
        raise ValueError('there is no zeroth prime')

    indx = 0
    for prme, indx in primes():
        if indx == number:
            return prme