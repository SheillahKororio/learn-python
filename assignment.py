print("Operations: +, -, , /, %, *")

# loop to keep calculator running
while True:
    
    operator = input("Enter operator (+,-,,/,%,*) or 'q' to quit: ").lower()

    if operator == "q":
        print("Calc terminated")
        break

    # --- TWO NUMBER OPERATIONS ---
    if operator in ["+", "-", "", "/", "%", "*"]:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if operator == "+":
                print(f"Result: {num1} + {num2} = {num1 + num2}")
            elif operator == "-":
                print(f"Result: {num1} - {num2} = {num1 - num2}")
            elif operator == "*":
                print(f"Result: {num1} * {num2} = {num1 * num2}")
            elif operator == "/":
                if num2 != 0:
                    print(f"Result: {num1} / {num2} = {num1 / num2}")
                else:
                    print("Error: Cannot divide by zero!")
            elif operator == "%":
                print(f"Result: {num1} % {num2} = {num1 % num2}")
            elif operator == "**":
                print(f"Result: {num1} * {num2} = {num1 * num2}")

        except ValueError:
            print("Invalid input! Please enter numbers only.")


    else:
        print("Invalid operator! Try again.")