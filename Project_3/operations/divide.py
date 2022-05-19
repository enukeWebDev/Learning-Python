def divide_number(x, y):
  
    # Keep track of the attempts - only allowed 3 attempts.
    attempts = 1
    while attempts <= 3:
        try:
            user_answer = int(input(f"{x} // {y} = "))
            if user_answer == (x // y):
                return True
                  
            else:
                attempts += 1
                print("EEE")
          
        except:
            attempts += 1
            print("EEE")

    print(f"{x} // {y} = {x // y}")