def react_quiz():

    print("Q1: What are the 2 ways to pass data to React components? \n")

    answer = input("A: ")
    correctAns = 0
    wrongAns = 0

    if answer.lower() == "props and context api" or "context api and props":
      print ("Your answer is ✅ ! \n")
      correctAns = correctAns + 1
      print(correctAns)
    
    else:
      print ("Your answer is ❌ ! \n")
      wrongAns = wrongAns + 1
      print(wrongAns)
    
    print("Q2: What is JSX? \n")

    answer = input("A: ")

    if answer.lower() != "javascript xml":
      print ("Your answer is ❌ ! \n")
      wrongAns = wrongAns + 1
      print(wrongAns)
    
    else:
      print ("Your answer is ✅ ! \n")
      correctAns = correctAns + 1
      print(correctAns)

    
    print("Q3: Name 2 types of React components? \n")

    answer = input("A: ")

    if answer.lower() == "function and class" or "class and function": 
      print ("Your answer is ✅ ! \n")
      correctAns = correctAns + 1
      print(correctAns)
    
    else:
      print ("Your answer is ❌ ! \n")
      wrongAns = wrongAns + 1
      print(wrongAns)

