def react_quiz():

    print("Q1: What are the 2 ways to pass data to React components? \n")

    answer = input("A: ")

    if answer.lower() == "props and context api" or "context api and props":
      print ("Your answer is ✅ ! \n")
    
    else:
      print ("Your answer is ❌ ! \n")

    
    print("Q2: What is JSX? \n")

    answer = input("A: ")

    if answer.lower() != "javascript xml":
      print ("Your answer is ❌ ! \n")
    
    else:
      print ("Your answer is ✅ ! \n")

    
    print("Q3: Name 2 types of React components? \n")

    answer = input("A: ")

    if answer.lower() == "function and class" or "class and function": 
      print ("Your answer is ✅ ! \n")
    
    else:
      print ("Your answer is ❌ ! \n")

