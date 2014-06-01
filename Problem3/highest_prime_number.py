def find_largest_prime(number_to_check):
        largest_prime_factor = 2
        while number_to_check > largest_prime_factor:
                if number_to_check % largest_prime_factor == 0:
                        number_to_check = number_to_check / largest_prime_factor
                        largest_prime_factor = 2
                else:
                        largest_prime_factor += 1
        return largest_prime_factor