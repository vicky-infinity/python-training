def divide():
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        result = num1 / num2
        print("Result:", result)

# This will catch the divide by 0 error
    except ZeroDivisionError:
        print("Cannot divide by zero")

# This is for invalid input type
    except ValueError as r:
        #print("Please enter numbers only")
        print(f"This is the error {r}")

    # finally:
    #     print("Program completed")

divide()