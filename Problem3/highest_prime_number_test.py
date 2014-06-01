import Problem3.highest_prime_number as highest_prime_number


def test_find_highest_prime_of_27():
    assert 7 == highest_prime_number.find_largest_prime(28)


def test_find_highest_prime_of_13195():
    assert 29 == highest_prime_number.find_largest_prime(13195)


def test_find_highest_prime_of_600851475143():
    assert 6857 == highest_prime_number.find_largest_prime(600851475143)


def test_number_is_prime():
    prime_number_to_check = 7
    assert prime_number_to_check == highest_prime_number.find_largest_prime(prime_number_to_check)