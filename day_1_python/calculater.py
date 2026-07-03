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
    operations = int(input(" choose the operation"))
    f1 = int(input("Enter the first number"))
    f2 = int(input("Enter Second Number"))

    if operations ==1:
        print(addi(f1,f2))
    if operations == 2:
        print(sub(f1,f2))
    if operations ==3:
        print(mul(f1,f2))
    if operations ==4:
        print(divi(f1,f2))

