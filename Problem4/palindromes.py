def is_palindrome(number_to_check):
    number_to_check_as_string = str(number_to_check)
    number_to_check_reversed_as_string = ''.join(reversed(number_to_check_as_string))

    if number_to_check_as_string == number_to_check_reversed_as_string:
        return True

    return False


def find_highest_palindrome_product_between(lower, upper):
    # uses list comprehension
    return max(x * y # variables
               for x in range(lower, upper) # input set
               for y in range(lower, upper) # input set
               if is_palindrome(x * y)) # optional predicate








