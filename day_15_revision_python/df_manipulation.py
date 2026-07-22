import pandas as pd

students = {
    101: {"name": "Aarav", "age": 21, "city": "Pune"},
    102: {"name": "Vihaan", "age": 22, "city": "Mumbai"},
    103: {"name": "Ishaan", "age": 20, "city": "Hyderabad"},
    104: {"name": "Aditya", "age": 23, "city": "Delhi"},
    105: {"name": "Krishna", "age": 21, "city": "Chennai"},
    106: {"name": "Rohan", "age": 22, "city": "Nagpur"},
    107: {"name": "Karan", "age": 20, "city": "Jaipur"},
    108: {"name": "Rahul", "age": 24, "city": "Pune"},
    109: {"name": "Harsh", "age": 21, "city": "Lucknow"},
    110: {"name": "Nikhil", "age": 22, "city": "Indore"},
    111: {"name": "Aman", "age": 23, "city": "Surat"},
    112: {"name": "Sahil", "age": 21, "city": "Bhopal"},
    113: {"name": "Yash", "age": 20, "city": "Ahmedabad"},
    114: {"name": "Deepak", "age": 24, "city": "Patna"},
    115: {"name": "Ritik", "age": 22, "city": "Kolkata"}
}

marks = {
    101: {"python": 85, "sql": 90, "ml": 88},
    102: {"python": 72, "sql": 80, "ml": 75},
    103: {"python": 91, "sql": 95, "ml": 93},
    104: {"python": 65, "sql": 70, "ml": 68},
    105: {"python": 78, "sql": 82, "ml": 80},
    106: {"python": 89, "sql": 87, "ml": 91},
    107: {"python": 55, "sql": 60, "ml": 58},
    108: {"python": 94, "sql": 92, "ml": 96},
    109: {"python": 83, "sql": 85, "ml": 84},
    110: {"python": 76, "sql": 79, "ml": 81},
    111: {"python": 68, "sql": 72, "ml": 70},
    112: {"python": 88, "sql": 91, "ml": 89},
    113: {"python": 81, "sql": 83, "ml": 85},
    114: {"python": 73, "sql": 75, "ml": 74},
    115: {"python": 97, "sql": 96, "ml": 98}
}

salary = {
    101: {"company": "TCS", "salary": 45000, "experience": 1},
    102: {"company": "Infosys", "salary": 52000, "experience": 2},
    103: {"company": "Google", "salary": 120000, "experience": 3},
    104: {"company": "Microsoft", "salary": 110000, "experience": 2},
    105: {"company": "Amazon", "salary": 98000, "experience": 2},
    106: {"company": "Capgemini", "salary": 50000, "experience": 1},
    107: {"company": "Wipro", "salary": 42000, "experience": 1},
    108: {"company": "Apple", "salary": 150000, "experience": 4},
    109: {"company": "IBM", "salary": 65000, "experience": 2},
    110: {"company": "Accenture", "salary": 58000, "experience": 2},
    111: {"company": "Cognizant", "salary": 47000, "experience": 1},
    112: {"company": "Oracle", "salary": 102000, "experience": 3},
    113: {"company": "Adobe", "salary": 115000, "experience": 3},
    114: {"company": "HCL", "salary": 49000, "experience": 1},
    115: {"company": "Meta", "salary": 160000, "experience": 5}
}

student_df = pd.DataFrame.from_dict(students, orient="index")
marks_df = pd.DataFrame.from_dict(marks, orient="index")
salary_df = pd.DataFrame.from_dict(salary, orient="index")

# print(salary_df.head())

salary_df["salary"]

salary_df[["114","115"]]