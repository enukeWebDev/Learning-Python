# from solution import solve_math_problems

def get_operation():
    operation = input("Please choose an operation +, -, *, //: ").strip()

    if operation in ("+", "-", "*", "//"):
        return operation
    
    else: 
        print("Invalid input.")

# def get_operation():
    
#     while True:
#         try:
#             operation = input("Please choose an operation +, -, *, //: ")
#             if operation in ("+", "-", "*", "//"):
#                 break
        
#         except ValueError:
#             print("Invalid input.")
#             continue
    
#     return operation

# def get_level():
#     while True:
#         try:
#             user_input = int(input("Level: "))

#             # Utilizing tuple because the value for level should only be 1, 2, 3 and should not be changed.
#             if user_input in (1, 2, 3):
#               break
#         except ValueError:
#             print("Invalid input.")
#             continue
            
#     return user_input


# def chooseCategory():

#     category = input("Please choose a category - ").lower()

#     if category == "javascript":
#       jsMessage()
#       js_quiz()
    
#     elif category == "python":
#       pythonMessage()
#       python_quiz()

#     elif category == "react":
#       reactMessage()
#       react_quiz()
    