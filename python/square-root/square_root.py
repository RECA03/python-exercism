def square_root(number):
    #Newton's methods. If guess is wrong, square root will ALWAYS be between the incorrect guess and square/guess
    guess = 1
    while guess*guess != number:
        guess = (guess + number/guess)/2
    return guess