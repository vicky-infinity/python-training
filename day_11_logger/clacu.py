# Calculater using the class and object concept
# Logging implimented

import logging

logger = logging.getLogger(__name__)####
logger.setLevel(logging.DEBUG)########

# Setting hander
file_handler = logging.FileHandler('calc.log')#########
#stream_handler = logging.StreamHandler()########

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')###########

file_handler.setFormatter(formatter)######
#stream_handler.setFormatter(formatter)#####

logger.addHandler(file_handler)##########
#logger.addHandler(stream_handler)########


logger.debug("This is the test")

import pandas as pd
logger.debug("Pandas liberary imported")
import numpy as np
logger.debug("numpy liberary imported")

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
    logger.debug("Show Information Function Declared")
    return print("Press 1 for Addition 2 for Substraction 3 for Multiplication 4 for Division")
    

logger.debug("While loop initiated")
while True:

    print("*"*30)
    info()
    print("*"*30)
    try:
        op = int(input("Enter The Operation 1,2,3 or 4: "))
        logger.debug(f"users choosen operation was {op}")
    except Exception as e:
        print("Enter the numbers only")
        logger.exception(f"Non num value entered {e}")
        logger.critical("User tryed entering the non numeric value loop initiated again")
        continue


    num1 = int(input("Enter First Number: "))
    logger.debug(f"The first number entered was {num1}")

    num2 = int(input("Enter Second Number: "))
    logger.debug(f"The Second number entered was {num2}")

    myob = math(op,num1,num2)
    logger.debug("If loop initiated")

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

    


