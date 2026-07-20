# Lamda function 

"""A lambda function is a small anonymous function in Python that can have any
 number of arguments but only one expression. It is typically used for short,
   simple operations where defining a full function with def would be unnecessary."""

# Syntax
# lambda arguments: expression
# lambda a,b: a+b

addi = lambda a,b: a+b

print(addi(5,5))
def apply(fx,b):
    result = fx+b
    return result

print(apply(lambda a,b,c: a+b+c, 5))

