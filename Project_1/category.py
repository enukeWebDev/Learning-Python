from categories.javascript import *
from categories.python import *
from categories.react import *
from animate import *

def chooseCategory():

    category = input("Please choose a category - ").lower()

    if category == "javascript":
      jsMessage()
      js_quiz()
    
    elif category == "python":
      pythonMessage()
      python_quiz()

    elif category == "react":
      reactMessage()
      react_quiz()
    
