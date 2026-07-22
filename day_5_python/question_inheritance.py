# Multi level inheritance


class personal_info():
    def __init__(self, name,phone):
        self.name = name
        self.phone = phone

    def show_persnal_info(self):
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
        self.name = name
        self.phone = phone
        self.dept_id = dept_id
        self.dept_name = dept_name
        self.salary_band = salary_band
        self.amount = amount
        
        

 