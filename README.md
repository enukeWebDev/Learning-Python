On going...

I recently graduated at Lighthouse Labs on Diploma on Full Stack Web Development. While I am waiting for the first perfect opportunity as a Junior Web Developer, I am currently building side projects using the MERN stack.

Also, I decided to continue learning. I am currently enrolled in CS50P - Introduction to Python Programming. This program is run by Harvard University.

This repository contains a simple projects in Python (on-top of the homework) - an application of my learning!

The main focus of these project are:

- explore the basic syntax of Python
- get comfortable on building different reusable modules in isolation then import
- explore some built-in libraries of Python
- explore on writing a unit test

1. Quiz App (short video clip demo below)

- https://imgflip.com/gif/6d46lj
- https://imgflip.com/gif/6d46s2
- https://imgflip.com/gif/6d46vi

* User is prompt to enter his/her name at the start of the app
* A welcome message with the name of the user will pop out
* A question will propmt user
  - yes will continue and prompt user to choose a category
  - no will exit the app
* There will be a few options for category to choose (still on going)
* After choosing the category
  - A question will pop out
  - If answer is correct - a message will show
  - If answer is wrong - a message will show
* Will add more categories & questions for each catergories
* Will implement a counter to count correct answers and wrong answers
* Output the final result (%)

2. Number Guessing Game

- This is one of my homework in CS50P (Harvard U)
- User is prompt for his/her name
- User is propmt for a positive integer (Level)
  - The Level serves as the upper limit of the range to guess the number from
  - The lower limit will always be 1
  - If user enters a negative number - user will be prompt again to enter an integer(Level)
  - If users enters a non integer (not a number) - user will be prompt again to enter an integer(Level)
- The program will generate a random number based on the range
- User will enter his/her guess
  - if lower than the number - message will show "Too small!"
  - if higher than the number - message will show "Too large!"
  - if number is the same - message will show "Just right!"
  - message shows to reveal the random number
- Program will exit once the guess is correct

3. Little Professor Game

!["Add"](https://github.com/enukeWebDev/Learning-Python/blob/main/Project_3/image/add.png?raw=true)

!["Multiply"](https://github.com/enukeWebDev/Learning-Python/blob/main/Project_3/image/multiply.png?raw=true)

- This is one of my homework in CS50P (Harvard U) that I expanded to imitate the actual Little Professor game. The assignment only covers the addition. This covers addition, subtraction, multiplication and division.
- User is prompt for level
  - Level 1 - generates number from 0 - 9
  - Level 2 - generates number from 10 - 99
  - Level 3 - generates number from 100 - 999
- User is propmt for the kind of operation (+, -, \*, //)
  - "+" - add number
  - "-" - subtract number
  - "\*" - multiply number
  - "//" - divide number (only give the whole number)
  - if user enter an incorrect operation, EEE message will show then user will be prompt again
- The program will generate a random quiz depending on the level and operation
- User will be prompt to answer each question
  - if answer is correct - it add to the correct answer and it will move to the next question
  - if wrong answer, it will prompt the user again to answer the same question
    - user have 3 attempts for each question to enter the correct answer
    - after 3 attempts and user did not get the correct answer, program will provide the correct answer and this will count as wrong answer
- Program will exit after 10 questions and will output how many correct answers the user have
