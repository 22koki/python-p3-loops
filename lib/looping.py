#!/usr/bin/env python3

# Task 1: happy_new_year
def happy_new_year():
    count = 10
    while count >= 1:
        print(count)
        count -= 1
    print("Happy New Year!")

# Task 2: square_integers
def square_integers(int_list):
    squared_numbers = [num ** 2 for num in int_list]
    return squared_numbers

# Task 3: fizzbuzz
def fizzbuzz():
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

# Test cases
happy_new_year()

numbers_to_square = [1, 2, 3, 4, 5]
squared_result = square_integers(numbers_to_square)
print(squared_result)

fizzbuzz()
