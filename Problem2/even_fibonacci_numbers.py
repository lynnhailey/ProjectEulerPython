list_of_fibonacci_numbers = [1, 2]
max_number = 4000000
next_number = 3
sum_even_numbers = 2

while next_number <= max_number:
    length = len(list_of_fibonacci_numbers)
    next_number = list_of_fibonacci_numbers[length-1] + list_of_fibonacci_numbers[length-2]

    if next_number <= max_number:
        list_of_fibonacci_numbers.append(next_number)

    if next_number % 2 == 0:
        sum_even_numbers += next_number

print(list_of_fibonacci_numbers)
print(sum_even_numbers)


