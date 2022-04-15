import time
import sys

def welcomeMessage(name):  
    w = "W E L C O M E . . . " + " ".join(name).upper() + " 🙂 !\n"

    for i in w:
      sys.stdout.write(i)
      sys.stdout.flush()
      time.sleep(0.2)

def mathMessage():

    m = "GENIUS - LET'S DO SOME MATH 📝 🔢 ✖️ 📐 🥇 . . . \n"

    for i in m:
      sys.stdout.write(i)
      sys.stdout.flush()
      time.sleep(0.1)

def movieMessage():

    mo = "MOVIE LOVER - LET'S SEE HOW MUCH MOVIE KNOWLEDGE DO YOU HAVE 🍿 👀 📽 . . . \n"

    for i in mo:
      sys.stdout.write(i)
      sys.stdout.flush()
      time.sleep(0.1)