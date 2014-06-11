from Problem6.sum_square_difference import sum_of_squares_up_to, sum_of_numbers_squared, \
    calculate_sum_of_numbers_squared_minus_sum_of_squares


def test_sum_of_squares_up_to_10():
    assert sum_of_squares_up_to(10) == 385


def test_sum_of_numbers_squared_for_10():
    assert sum_of_numbers_squared(10) == 3025


def test_calculate_sum_of_numbers_squared_minus_sum_of_squares_for_10():
    assert calculate_sum_of_numbers_squared_minus_sum_of_squares(10) == 2640


def test_calculate_sum_of_numbers_squared_minus_sum_of_squares_for_100():
    assert calculate_sum_of_numbers_squared_minus_sum_of_squares(100) == 25164150