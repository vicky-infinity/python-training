# Q1. Student Grades
# Create a class Student with:

# attributes: name, marks
# method is_pass() → returns True if marks ≥ 40

# Create 5 students and print names of students who passed.

class Student():
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_pass(self):
        if self.marks >= 40:
            return f"Student is Passed: {self.name}"
        # else:
        #     return f"Student is failed"

ob1 = Student("Harsh", 60)
ob2 = Student("Mohit",40)
ob3 = Student("Saket",50)
ob4 = Student("Kartik",70)
ob5 = Student("Dipak",20)

objects = [ob1, ob2, ob3, ob4, ob5]

for i in objects:
    print(i.is_pass())