def python_quiz():
  
    print("Q1: Which data types allow slicing? \n")

    print("a. str\t b. tuple\t c. str\t d. All of the above\n")
    answer = input("A: ")

    if answer != "d":
      print ("Your answer is ❌ ! \n")
    
    else:
      print ("Your answer is ✅ ! \n")

    
    print("Q2: What will be the output of the following code? \
      \n\n\tinput_dictionary = {\n\t\t'X': 1994, \n\t\t'Y': 1110, \n\t\t'X': 1094 \
      \n\t} \n\tprint(input_dictionary['X']) \n")

    print("a. 1994\t b. None\t c. 1094\t d. Runtime time error due to duplicate keys \n")
    answer = input("A: ")

    if answer != "c":
      print ("Your answer is ❌ ! \n")
    
    else:
      print ("Your answer is ✅ ! \n")


    print("\nQ3: What will be the output of the following code? \
      \n\n\tpow_output = pow(2, 5, 9) \n\tprint(pow_output) \n")

    print("a. 5\t b. Error\t c. 3\t d. 288\n")
    answer = input("A: ")

    if answer != "a":
      print ("Your answer is ❌ ! \n")
    
    else:
      print ("Your answer is ✅ ! \n")
      
    
    print("\nQ4: What will be the output of the following code? \
      \n\n\ta = [3, 4, 5] \n\tb = [6, 7, 8] \
      \n\tprint(a.sum(b)) \n")

    print("a. Error\t b. [9, 11, 13]\t c. 33\t d. None of the above\n")
    answer = input("A: ")

    if answer != "a":
      print ("Your answer is ❌ ! \n")
    
    else:
      print ("Your answer is ✅ ! \n")


    print("\nQ5: What will be the output of the following code? \
      \n\n\ta = [10, 5, 4, 12] \n\tb = a[0] ** a[2] \
      \n\tprint(b) \n")

    print("a. 10000\t b. 400\t c. 100000\t d. Error\n")
    answer = input("A: ")

    if answer != "a":
      print ("Your answer is ❌ ! \n")
    
    else:
      print ("Your answer is ✅ ! \n")