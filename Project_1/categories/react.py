from counter import *

def react_quiz():

    correctAns = 0
    wrongAns = 0
    
    print("Q1: What are the 2 ways to pass data to React components? \n")

    answer = input("A: ")
   

    if answer.lower() == "props and context api" or "context api and props":
      print ("Your answer is ✅ ! \n")
      correctAns += 1
    
    else:
      print ("Your answer is ❌ ! \n")
      wrongAns += 1
      
    
    print("Q2: What is JSX? \n")

    answer = input("A: ")

    if answer.lower() != "javascript xml":
      print ("Your answer is ❌ ! \n")
      wrongAns += 1
    
    else:
      print ("Your answer is ✅ ! \n")
      correctAns += 1

    
    print("Q3: Name 2 types of React components? \n")

    answer = input("A: ")

    if answer.lower() == "function and class" or "class and function": 
      print ("Your answer is ✅ ! \n")
      correctAns += 1
    
    else:
      print ("Your answer is ❌ ! \n")
      wrongAns += 1

    
    
