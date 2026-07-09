# Error Handling

def greet():
    try:
        number = int(input(("Please Enter you Number")))
        result = number + 10
        print(f"Your Number {number} plus 10 is {result}")
    except:
        print("Please enter the number only")
    finally:
        print("Finally block i always execute")

greet()