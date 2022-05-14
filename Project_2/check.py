# Validate/check/compare the number.

def check_number(n):
    while True:
        try:
            guess = int(input("Guess: "))
            if guess > 0:
                if guess < n:
                    print("Too small!")
                elif guess > n:
                    print("Too large!")
                else:
                    print("Just right!")
                    break
        
        except:
            continue 
