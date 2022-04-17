from categories.javascript import *
from categories.movie_q import *
from categories.iq_q import *
from animate import *

def chooseCategory():

    category = input("Please choose a category - ").lower()

    if category == "javascript":
      mathMessage()
      js_quiz()
    
    elif category == "movie":
      movieMessage()
      movie_quiz()

    elif category == "iq":
      iqMessage()
      iq_quiz()
    
