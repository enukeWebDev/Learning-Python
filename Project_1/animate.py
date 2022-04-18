import time
import sys

def welcomeMessage(name):  
    w = "W E L C O M E . . . " + " ".join(name).upper() + " 🙂 !\n"

    for i in w:
      sys.stdout.write(i)
      sys.stdout.flush()
      time.sleep(0.2)

def goodbyeMessage(name):  
    g = "G O O D B Y E . . . " + " ".join(name).upper() + " !\n"

    for i in g:
      sys.stdout.write(i)
      sys.stdout.flush()
      time.sleep(0.2)

def jsMessage():

    m = "\nLET'S LEARN JAVASCRIPT . . . \n"

    for i in m:
      sys.stdout.write(i)
      sys.stdout.flush()
      time.sleep(0.1)

def pythonMessage():

    mo = "\nLET'S LEARN PYTHON . . . \n"

    for i in mo:
      sys.stdout.write(i)
      sys.stdout.flush()
      time.sleep(0.1)

def reactMessage():

    iq = "\nLET'S LEARN REACT . . . \n"

    for i in iq:
      sys.stdout.write(i)
      sys.stdout.flush()
      time.sleep(0.1)