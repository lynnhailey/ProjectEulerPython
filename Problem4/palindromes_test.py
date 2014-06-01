import Problem4.palindromes as palindromes


def test_is_palindrome_success():
    assert palindromes.is_palindrome(99) is True
    assert palindromes.is_palindrome(909) is True
    assert palindromes.is_palindrome(9009) is True


def test_is_palindrome_failure():
    assert palindromes.is_palindrome(12) is False
    assert palindromes.is_palindrome(123) is False
    assert palindromes.is_palindrome(1223) is False


def test_find_highest_palindrome_product_of_two_digit_numbers():
    assert 9009 == palindromes.find_highest_palindrome_product_between(10, 100)


def test_find_highest_palindrome_product_of_three_digit_numbers():
    assert 906609 == palindromes.find_highest_palindrome_product_between(100, 1000)