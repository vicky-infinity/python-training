# # Write a code to differentiate between overriding and overloading

# class a():
#     def math(self,a,b):
#         result = a+b
#         return result
        
# class b(a):

#     def math(self,a,b):
#         result = a - b
#         return result
    
# obb1 = a()
# obb2 = b()

# print(obb1.math(5,1))
# print(obb2.math(5,1))

###################################################
# Over loading
# Python doesnt support the method overloading but we can simulate it using the default arguments


class calculator:

    def math(self, a, b=0):
        return a + b


obj = calculator()

print(obj.math(5))
print(obj.math(5, 10))


