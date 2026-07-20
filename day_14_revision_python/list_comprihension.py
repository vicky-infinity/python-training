# List Comprihension

"""List comprehension is a concise and Pythonic way to create a new 
list by iterating over an iterable and optionally applying a condition
or transformation in a single line.

# Instead of writing multiple lines using a for loop and append(), 
# list comprehension lets you achieve the same result in one readable 
# statement.
"""
# General Syntax
# [expression for item in iterable]

# New list in range
newlst = [i for i in range(1,11)]

# New list of squeres
sqlst = [i*i for i in range(1,11)]

# New list with cubes
cubelst = [i*i*i for i in range(1,11)]
# Empty list, if else in list comprihension
emplst = []

[emplst.append(i) if i<=3 else emplst.append("Grater then 3") for i in range(1,11)]

# Printing all statements
print(f"This is new lst {newlst}")
print(f"This is sqlst {sqlst}")
print(f"This is cubelst {cubelst}")
print(f"This is emlstlst {emplst}")


# if in list comprihension Check if number is divisible by 5 

divby5 = [i for i in range(1,51) if i%5 == 0]

print(f"Divby5 {divby5}")


