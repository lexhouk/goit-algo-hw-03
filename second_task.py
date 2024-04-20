import random


def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    '''
    Generate unique random numbers for the lottery.

    :param min: integer
    :param max: integer
    :param quantity: integer

    :return: list
    '''

    try:
        # The smallest generated number must be greater than or equal to one.
        is_min_valid = min > 0

        # The largest generated number must be less than or equal to one
        # thousand.
        is_max_valid = min <= max < 1001

        # Calculate the amount of numbers in sequence.
        max_quantity = max - min + 1

        # The number of generated numbers must not exceed the number of numbers
        # between the smallest and largest numbers.
        is_quantity_valid = quantity <= max_quantity
    
    except TypeError:
        print('All arguments must be integer numbers!')
        return []
    
    if is_min_valid and is_max_valid and is_quantity_valid:
        # There is no point in guessing numbers when they are at their maximum,
        # so it is enough to just return a sorted sequence.
        if quantity == max_quantity:
            return list(range(min, max + 1))
        
        numbers = set()

        while len(numbers) < quantity:
            numbers.add(random.randint(min, max))

        return sorted(list(numbers))
    
    return []
