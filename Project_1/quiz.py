from category import *
from animate import *

def main():
    welcomeMessage()

    user = input("Do you want to have fun? ").lower()
    categoryList = ["Math", "Movie", "IQ"]

    if user != "yes":
      exit()

    else:
      chooseCategory()
      

if __name__ == "__main__":
    main()