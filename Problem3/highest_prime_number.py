def find_highest_prime_number(find_prime):
    if find_prime % 2 == 0:
        number = find_prime - 1
    else:
        number = find_prime

    while number >= 3:
        if find_prime % number == 0:
            if is_prime_number(number):
                return number
        number = number - 2


def is_prime_number(number_to_check):
    count = 3
    while count < number_to_check:
        if number_to_check % count == 0:
            return False
        count = count + 2

    return True
