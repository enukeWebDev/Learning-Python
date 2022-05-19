import random
from level import get_level
# from operation import get_operation
from math_prob import generate_math_problems


def main():
    user_input = get_level()
    # get_operation()
    final_score = generate_math_problems(user_input)
    print(f"Score: {final_score}")


if __name__ == "__main__":
    main()