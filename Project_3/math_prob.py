from generate_integer import generate_integer
from operation import get_operation
from add import add_number
from subtract import subtract_number
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
            check_answer = add_number(x, y)
            if check_answer:
                user_score += 1
            math_problems_count += 1
        
        return user_score

    elif x == "-":
        while math_problems_count <= 10:
            x, y = generate_integer(user_input)
            check_answer = subtract_number(x, y)
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