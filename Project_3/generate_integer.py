import random

def generate_integer(user_input):
    if user_input == 1:
        num1, num2 = random.randint(0,9), random.randint(0,9)
    elif user_input == 2:
        num1, num2 = random.randint(10,99), random.randint(10,99)
    else:
        num1, num2 = random.randint(100,999), random.randint(100,999)

    return num1, num2