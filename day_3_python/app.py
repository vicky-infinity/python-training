# Calculater using the class and object concept


class math:
    def __init__(self,op, num1, num2):
        self.op = op
        self.num1 = num1
        self.num2 = num2

    def add(self):
        result = self.num1 + self.num2
        return result
    
    def sub(self):
        result  = self.num1 - self.num2
        return result
    
    def mul(self):
        result = self.num1 * self.num2
        return result
    
    def div(self):
        result = self.num1 / self.num2
        return result

def info():
    return print("Press 1 for Addition 2 for Substraction 3 for Multiplication 4 for Division")



while True:

    print("*"*30)
    info()
    print("*"*30)

    op = int(input("Enter The Operation 1,2,3 or 4: "))
    num1 = int(input("Enter First Number: "))
    num2 = int(input("Enter Second Number: "))

    myob = math(op,num1,num2)
    
    if op == 1:
        result = myob.add()
        print(result)
    elif op ==2:
        result = myob.sub()
        print(result)
    elif op ==3:
        result = myob.mul()
        print(result)
    elif op ==4:
        result = myob.div()
        print(result)
    else:
        print("Invalid Input Please choose the operation for the list only")

    


