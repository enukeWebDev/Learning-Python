# Ask user for a level that will be the basis of how many digits the math problems will generate.
def get_level():
    while True:
        try:
            user_input = int(input("Level: "))
            if user_input in (1, 2, 3):
              break
        except ValueError:
            print("Invalid input.")
            continue
            
    return user_input