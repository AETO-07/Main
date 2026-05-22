while True:
    expression = input("Enter calcuation (e.g 2 + 4 _ 5 * 6 / 8)")
    if any(char.isalpha() for char in expression):
         print("Invalid Input (Letters not allowed)")
         continue
    
    operators = ["+", "-", "/", "*"]
    if any(op1 + op2 in expression for op1 in operators for op2 in operators):
         print("Invalid Expressions (double operators)")
         continue
    # works the same way:
    # for op1 in operators:
        #for op2 in operators:
            #if op1 + op2 in expression:
                # print("double operators")
    try:
        result = eval(expression)
        print("Result:", result)
        
    except ZeroDivisionError:
        print("Cannot divide by zero")

    except: 
        print("Invalid expression!")

    again = input("Continue (y/n): ").strip().lower()
    if again != "y":
            break    