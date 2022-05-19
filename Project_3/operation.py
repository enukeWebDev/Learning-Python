# Ask user to choose an operation.
def get_operation():

  while True:
    try:
      operation = input("Please choose an operation +, -, *, //: ").strip()
      if operation in ("+", "-", "*", "//"):
          break

    except ValueError:
          print("Invalid input.")
          continue
  
  return operation
