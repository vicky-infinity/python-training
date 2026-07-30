class MyClass:
    def __init__(self):
        # Protected variable (indicated by a single leading underscore)
        self._protected_var = "I am a Protected Variable"
        
        # Private variable (indicated by a double leading underscore)
        self.__private_var = "I am a Private Variable"

# 1. Instantiate the class object
obj = MyClass()

# 2. Printing the protected variable outside the class
# Python allows direct access, though it is discouraged by convention.
print(obj._protected_var)

# 3. Printing the private variable outside the class
# Attempting `print(obj.__private_var)` directly will raise an AttributeError.
# Instead, you must use Name Mangling: _ClassName__variableName
print(obj._MyClass__private_var)