# Write a code to differentiate between overriding and overloading

class a():
    def __init__(self):
        pass
    
    def math(a,b):
        result = a+b
        return result
        
class b(a):

    def math(f1, f2):
        result = f1-f2
        return result

obb = b()

obb.math(2,5)