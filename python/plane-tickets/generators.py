"""Functions to automate Conda airlines ticketing system."""

def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    Parameters:
        number (int): Total number of seat letters to be generated.

    Returns:
        generator: A generator that yields seat letters.

    Note:
        Seat letters are generated from A to D.
        After D the sequence starts again with A.
        For example: A, B, C, D, A, B

    """

    letters = ["A","B","C","D"]
    letter_id = 0
    for _ in range(number): # "_" serves as a loop variable that python knows i won't use anywhere else
        if letter_id == 4:
            letter_id = 0
        letter = letters[letter_id]
        yield letter
        letter_id += 1


def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    Parameters:
        number (int): The total number of seats to be generated.

    Returns:
        generator: A generator that yields seat numbers.

    Note:
        A seat number consists of the row number and the seat letter.
        There is no row 13, and each row has 4 seats.

        Seats should be sorted from low to high.
        For example: 3C, 3D, 4A, 4B

    """

    seat_number = 1
    counter = 1
    seat_letters = generate_seat_letters(number)
    for _ in range(number):
        if counter == 5:
            seat_number += 1
            if seat_number == 13:
                seat_number += 1
            counter = 1
        counter += 1
        yield str(seat_number) + next(seat_letters, None) #if generator for seat letters is exhausted, None is returned


def assign_seats(passengers):
    """Assign seats to passengers.

    Parameters:
        passengers (list[str]): A list of strings containing names of passengers.

    Returns:
        dict: With passenger names as keys and seat numbers as values.
        Example output: {"Adele": "1A", "Björk": "1B"}

    """

    seat_amount = len(passengers)
    seats = generate_seats(seat_amount)
    seat_assignations = {}
    for passenger in passengers:
        seat_assignations[passenger] = next(seats)
    
    return seat_assignations
        

def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    Parameters:
        seat_numbers (list[str]): A list of seat numbers.
        flight_id (str): A string containing the flight identifier.

    Returns:
        generator: A generator that yields 12 character long ticket codes.

    """
    for seat in seat_numbers:
        yield seat + flight_id + "000000000000"[len(seat+flight_id):]