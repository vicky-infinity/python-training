import pandas as pd

df = pd.read_csv('employees.csv')

def sep():
    print("*"*100)
    print("*"*100)


sep()
# Check top 5
print("Top 5 records")
print(df.head())
sep()


# Info about the df

df.info()
sep()
print(df.shape) 
sep()
print(df.columns)  
sep()

# Print multiple columns
print(df[["emp_id", "salary"]])

sep()
# Calculating highest salary
print(df["salary"].max())
