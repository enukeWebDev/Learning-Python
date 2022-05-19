from solution import solve_math_problems
from generate_integer import generate_integer
from operation import *
from subtract import subtract
from multiply import multiply_number
from divide import divide_number

# Generates 10 math problems based on the value of the user input and the operation.
def generate_math_problems(user_input):
    math_problems_count = 1
    user_score = 0

    x = get_operation()

    if x == "+":
        while math_problems_count <= 10:
            x, y = generate_integer(user_input)
            check_answer = solve_math_problems(x, y)
            if check_answer:
                user_score += 1
            math_problems_count += 1
        
        return user_score

    elif x == "-":
        while math_problems_count <= 10:
            x, y = generate_integer(user_input)
            check_answer = subtract(x, y)
            if check_answer:
                user_score += 1
            math_problems_count += 1
        
        return user_score

    elif x == "*":
        while math_problems_count <= 10:
            x, y = generate_integer(user_input)
            check_answer = multiply_number(x, y)
            if check_answer:
                user_score += 1
            math_problems_count += 1
        
        return user_score

    else:
        while math_problems_count <= 10:
            x, y = generate_integer(user_input)
            if y >= 1:
                check_answer = divide_number(x, y)
                if check_answer:
                    user_score += 1
                math_problems_count += 1
        
        return user_score

 # x = get_operation()
    # if x == "+":
    # # Keep track of the math problems - only 10 math problems.
    #     math_problems_count = 1

    #     # Keep track of the score of the user - 1 point every correct answer.
    #     user_score = 0

    #     while math_problems_count <= 10:
    #         x, y = generate_integer(user_input)
    #         check_answer = solve_math_problems(x, y)

    #         if check_answer:
    #             user_score += 1
            
    #         math_problems_count += 1
        
    #     return user_score
