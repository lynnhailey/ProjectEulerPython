def sum_of_squares_up_to(number):
    sum = 0

    for to_square in range(1, number + 1):
        square = to_square * to_square
        sum += square

    return sum


def sum_of_numbers_squared(number):
    sum = 0

    for count in range(1, number + 1):
        sum += count

    return sum * sum


def calculate_sum_of_numbers_squared_minus_sum_of_squares(number):
    return sum_of_numbers_squared(number) - sum_of_squares_up_to(number)