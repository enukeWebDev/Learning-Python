def get_level():
    while True:
        try:
            user_input = int(input("Level: "))

            # Utilizing tuple because the value for level should only be 1, 2, 3 and should not be changed.
            if user_input in (1, 2, 3):
              break
        except ValueError:
            print("Invalid input.")
            continue
            
    return user_input