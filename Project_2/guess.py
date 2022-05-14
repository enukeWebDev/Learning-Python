# Validate that the input is a positive integer.
# Generate the random number.
# Guess the number.

from random import randint
from check import check_number

def guess_number():
    while True:
        try:
            user_input = int(input("Level: "))
            if user_input > 0:
                break

        except:
            continue

    generate_number = randint(1, user_input)
    check_number(generate_number)

