def addi(a,b):
    c = a + b
    return c

def sub(a,b):
    c = a - b
    return c

def divi(a,b):
    c = a / b
    return c

def mul(a,b):
    c = a * b
    return c


while True:
    print("press 1 for add 2 for sub 3 for mul 4 for div")
    print("*"*50)
    operations = int(input("Choose the Operation: "))
    f1 = int(input("Enter the First number: "))
    f2 = int(input("Enter Second Number: "))

    if operations ==1:
        print(addi(f1,f2))
    elif operations == 2:
        print(sub(f1,f2))
    elif operations ==3:
        print(mul(f1,f2))
    elif operations ==4:
        print(divi(f1,f2))
    else:
        print("Envalid operation" \
        " Please choose form the following list Thank You")

