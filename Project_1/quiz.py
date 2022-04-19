from category import *
from animate import *
from counter import * 

def main():

    user = input ("What is your name? ")
    welcomeMessage(user)

    userChoice = input("Do you want to have fun? ").lower()
    categoryList = ["Javascript", "Python", "React"]

    if userChoice != "yes":
      goodbyeMessage(user)
      exit()

    else:
      chooseCategory()

    print(counter())

if __name__ == "__main__":
    main()