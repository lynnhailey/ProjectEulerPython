def smallest_multiplier_up_to(number):
    count = number

    while not can_be_divided_by_all_numbers_in_range(count, number):
        count += number

    return count


def can_be_divided_by_all_numbers_in_range(number_to_check, number_range):
    for to_try in range(1, number_range + 1):
        if number_to_check % to_try != 0:
            return False

    return True
