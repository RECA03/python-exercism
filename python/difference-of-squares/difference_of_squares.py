def square_of_sum(number):

    sum_to_square = 0
    for num in range(number+1):
        sum_to_square += num
    
    return sum_to_square**2


def sum_of_squares(number):
    
    squares = []
    for num in range(number+1):
        squares.append(num**2)
    
    return sum(squares)


def difference_of_squares(number):
    sum_squared = square_of_sum(number)
    squares_sum = sum_of_squares(number)

    return sum_squared - squares_sum
