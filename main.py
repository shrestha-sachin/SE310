team_name = "GDGHackers"

def addition(number1, number2):
  print("We are adding " + str(number1) + " and " + str(number2))
  return number1 + number2

def subtraction(number1, number2):
  print("We are subtracting " + str(number2) + " from " + str(number1))
  return number1 - number2

def multiplication(number1, number2):
  print(f"We are multiplying {number1} and {number2}")
  return number1 * number2

def integer_division(number1, number2, error_msg=None):
  print("We are performing integer division on " + str(number1) + " and " + str(number2))
  if number2 == 0:
    raise ZeroDivisionError(error_msg or "Cannot divide by zero")
  return number1 // number2

def division(number1, number2, error_msg=None):
    print("We are performing division on " + str(number1) + " and " + str(number2))
    if number2 == 0:
      raise ZeroDivisionError(error_msg or "Cannot divide by zero")
    return number1 / number2

def SQRT(number, error_msg=None):
  print("We are calculating the square root of " + str(number))
  if number < 0:
    raise ValueError(error_msg or "Square root of negative number should raise an error")
  return number ** 0.5


def calculator():
  print("Calculator by team =  " + team_name)
  print("Choose the operation you want to perform: ")
  print("1. Addition")
  print("2. Subtraction")
  print("3. Multiplication")
  print("4. Division")
  print("5. Integer Division")
  print("6. Square Root")
  print("7. Exponent")

  choice = int(input("Enter your choice: "))
  
  if choice == 1:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print(f"Result: {addition(num1, num2)}\n")
  elif choice == 2:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print(f"Result: {subtraction(num1, num2)}\n")
  elif choice == 3:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print(f"Result: {multiplication(num1, num2)}\n")
  elif choice == 4:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print(f"Result: {division(num1, num2)}\n")
  elif choice == 5:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print(f"Result: {integer_division(num1, num2)}\n")
  elif choice == 6:
    num = float(input("Enter a number: "))
    print(f"Result: {SQRT(num)}\n")
  else:
    print("Invalid choice!")


if __name__ == "__main__":
  calculator()