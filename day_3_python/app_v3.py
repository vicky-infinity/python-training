#1. Inheritance
#2. Encapsulation
#3. Polymorphism
#4. Abstraction


# Inheritance 

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name}")

# This is the child node
class Student(Person):

    def show_marks(self):
        print("Marks: 90")