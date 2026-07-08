# Multi level inheritance


class personal_info():
    def __init__(self, name,phone):
        self.name = name
        self.phone = phone

    def show_personal_info(self):
        result = f"The name is: {self.name} and Contact no: {self.phone}"
        return result


class DeptInfo(personal_info):
    def __init__(self,name, phone, dept_id, dept_name):
        super().__init__(name, phone)
        self.dept_id = dept_id
        self.dept_name = dept_name
    
    def show_dept_info(self):
        result = (f"The dept id is: {self.dept_id} This is the dept name: {self.dept_name}")
        return result


class Salary_info(DeptInfo):
    def __init__(self,name, phone, dept_id, dept_name, salary_band, amount):
        super().__init__(name, phone,dept_id,dept_name)
        self.salary_band = salary_band
        self.amount = amount

    def show_salary_info(self):
        result = f"The salary of the {self.name} is {self.amount} and the salry band is {self.salary_band}"
        return result
    
# This is the object of the base class thats why we can only access these 2 mentods
# To access all the mothods we have to create the object of the most derived class
# In our case it is salary info class

# emp = personal_info("Suresh",8989809099)

# ff = emp.show_personal_info()
# print(ff)


# This is the most derived class
# Here we created the object from only one class and inheriting the methods of the base classed from the derived class
# emp2 = Salary_info("Sanjay",8988909898,10056,"HR","5-10",60550)

# print(emp2.show_personal_info())
# print(emp2.show_dept_info())
# print(emp2.show_salary_info())


emp3 = DeptInfo("ROY",9099989898,78001,"IT")

# print(emp3.show_personal_info())

print(emp3.show_salary_info())