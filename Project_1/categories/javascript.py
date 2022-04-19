from counter import *

def js_quiz():

    correctAns = 0
    wrongAns = 0

    print("\nQ1: What will be the output of the following code snippet? \
              \n\tlet sum = 0; \n\tconst a = [1 ,2 3]; \n\ta.forEach(getSum); \
              \n\tprint(sum); \n\tfuntion getSum(ele) {\n\t\tsum += elem \n\t}\n")
    print("a. 6\t b. 1\t c. 2\t d. None\n")
    answer = input("A: ").lower()

    if answer != "a":
      print ("Your answer is ❌ ! \n")
      wrongAns += 1
    
    else:
      print ("Your answer is ✅ ! \n")
      correctAns += 1
  
    print("Q2: What will be the output of the following code snippet? \
              \n\ta = [1, 2, 3, 4, 5]; \n\t print(a.slice(2,4));\n")
    print("a. 3, 4\t b. 2, 3\t c. 3, 4, 5\t d. 2, 3, 4\n")
    answer = input("A: ").lower()
 
    if answer != "a":
      print ("Your answer is ❌ ! \n")
      wrongAns += 1
    
    else:
      print ("Your answer is ✅ ! \n")
      correctAns += 1
  
    print ("\nQ3: What will be the output of the following code snippet? \
        \n\tlet a = [1, 2, 3, 4, 5, 6]; \n\tlet left = 0, right = 5; \
          \n\tlet found = false; \n\tlet target = 5; \n\n\twhile(left <= right) { \
            \n\t\tlet mid = Math.floor((left + right) / 2); \n\t\tif(a[mid] == target) { \
              \n\t\t\tfound = true; \n\t\t\tbreak; \
                \n\t\t} \n\t\telse if (a[mid] < target) {\n\t\t\tleft = mid + 1; \n\t\t} \
                  \n\t\telse {\n\t\t\tright = mid - 1; \n\t\t} \
                    \n\tif (found) {\n\t\tprint('YES'); \n\t} \n\telse {\n\t\t  print('NO'); \n\t}\n")
  

    print("a. YES\t b. NO\t c. Syntax Error\t d. None\n")
    answer = input("A: ").lower()
 
    if answer != "a":
      print ("Your answer is ❌ ! \n")
      wrongAns += 1
    
    else:
      print ("Your answer is ✅ ! \n")
      correctAns += 1
    

    print("Q4: What happens when we run this code? \
              \n\tfunction dog() { \n\t\t print('I am a dog');\n\t} \
              \n\tdog.sound = 'Bark';\n")

    print("a. Syntax Error\t b. 'I am a dog'\t c. ReferenceError\t d. Nothing happens\n")
    answer = input("A: ").lower()
 
    if answer != "d":
      print ("Your answer is ❌ ! \n")
      wrongAns += 1
    
    else:
      print ("Your answer is ✅ ! \n")
      correctAns += 1


    print("Q5: What will be the output of the following code snippet? \
              \n\tfunction sum(a, b) {\n\t\treturn a + b;\n\t}\n\n\tsum(1, '2');\n")

    print("a. 12\t b. Nothing\t c. SyntaxError\t d. 12\n")
    answer = input("A: ").lower()
 
    if answer != "b":
      print ("Your answer is ❌ ! \n")
      wrongAns += 1
    
    else:
      print ("Your answer is ✅ ! \n")
      correctAns += 1

    
    print(counter(correctAns, wrongAns))