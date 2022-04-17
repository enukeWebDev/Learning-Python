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

def mathMessage():

    m = "\nLET'S LEARN JAVASCRIPT . . . \n"

    for i in m:
      sys.stdout.write(i)
      sys.stdout.flush()
      time.sleep(0.1)

def movieMessage():

    mo = "\nLET'S SEE HOW MUCH MOVIE KNOWLEDGE DO YOU HAVE 🍿 👀 📽 . . . \n"

    for i in mo:
      sys.stdout.write(i)
      sys.stdout.flush()
      time.sleep(0.1)

def iqMessage():

    iq = "\nLET'S TEST YOUR I.Q. 👨‍💻 . . . \n"

    for i in iq:
      sys.stdout.write(i)
      sys.stdout.flush()
      time.sleep(0.1)