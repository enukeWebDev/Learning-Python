from categories.math_q import *
from categories.movie_q import *
from animate import *

def chooseCategory():

    category = input("Please choose a category - ").lower()

    if category == "math":
      mathMessage()
      math_quiz()
    
    elif category == "movie":
      movieMessage()
      movie_quiz()
        