# Txt 1 problem 1

# --------------------------------------------------
# Q1. Student Attendance System
# --------------------------------------------------

# Create a class Student.

# Attributes:
# - name
# - attendance_percentage

# Methods:
# - is_eligible() → returns True if attendance is at least 75%.

# Tasks:

# - Create 6 students.
# - Store all students in a list.
# - Build a dictionary {student_name: attendance_percentage} for eligible students.
# - Print the dictionary.

class Student():
    def __init__(self, name, attendance_percentage):
        self.name = name
        self.attendance_percentage =attendance_percentage
    
    def is_eligible(self):
        if self.attendance_percentage >= 75:
            return True
        else:
            return False

std1 = Student("st1",76)
std2 = Student("Stu2",60)
std3 = Student("Stu3",50)
std4 = Student("Stu4",80)
std5 = Student("Stu5",75)
std6 = Student("Stu6",90)


students = [std1,std2,std3,std4,std5,std6]

std_dict ={}

for student in students:
    if student.is_eligible():
        # This is the key and    This is the value of the key 
        std_dict[student.name] = student.attendance_percentage
        # std_dict["Student_name"].append(student.name) 
        # std_dict["Attendance_percentage"].append(student.attendance_percentage)
        
print(std_dict)



