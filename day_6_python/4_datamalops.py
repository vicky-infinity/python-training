# Data manipulation 
import pandas as pd

df = pd.read_csv("employees.csv")

print(df.info())



print(df[df['salary'] > 50000])
maxbonus = df['bonus'].max()

print("This is the highes bonus: ", maxbonus)

# conditional 
print(df[(df['Salary'] > 50000) & (df['Age'] > 25)])

# How to rename the column name
# df.rename(columns={'old column': 'new column'})]








