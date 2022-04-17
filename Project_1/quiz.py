from category import *
from animate import *

def main():

    user = input ("What is your name? ")
    welcomeMessage(user)

    userChoice = input("Do you want to have fun? ").lower()
    categoryList = ["Javascript", "React", "Python"]

    if userChoice != "yes":
      goodbyeMessage(user)
      exit()

    else:
      chooseCategory()


if __name__ == "__main__":
    main()