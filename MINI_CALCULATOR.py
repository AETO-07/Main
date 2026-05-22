while True:
    try:
        num1 = float(input("Enter  first number:"))
        op = input("Enter your operator(+, -, *, /)")
        num2 = float(input("Enter  second number"))

        if op == "+":
                print("Result:", num1 + num2)
        elif op == "-":
                #print("Result:" + num1 - num2 ) works same
                print("Result:", num1 - num2)
        elif op == "*":
              print("Result:", num1 * num2)
        elif op == "/":
            if num2 == 0:
                    print("Cannot divide by zero!")
            else:
                    print("Result:", num1 / num2)
    except ValueError:
          print("Invalid input, try again!")
    
    again = input("Continue? (y/n): ")
    if again.lower() != "y":
          break
