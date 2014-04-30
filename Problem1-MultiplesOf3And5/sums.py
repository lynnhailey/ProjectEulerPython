def get_sum_of_multipliers_of_3_and_5(number):
    count = 2
    sum_of_multipliers = 0
    while count < number:
        if count % 3 == 0 or count % 5 == 0:
            print(count)
            sum_of_multipliers += count
        count += 1
    #if number is 10 answer should be 23
    return sum_of_multipliers