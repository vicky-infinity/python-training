import pandas as pd
# This is the left table
df1 = pd.DataFrame({
    'Emp_ID': [1, 2, 3, 4],
    'Name': ['John', 'Alice', 'Bob', 'David']
})

# This is the right table
df2 = pd.DataFrame({
    'Emp_ID': [3, 4, 5, 6],
    'Salary': [50000, 60000, 70000, 80000]
})

inner_df = pd.merge(df1, df2, on='Emp_ID', how='inner')
print("\nThis is the lnner Join")
print(inner_df)

left_df = pd.merge(df1, df2, on='Emp_ID', how='left')
print("\nThis is the left Join")
print(left_df)

right_df = pd.merge(df1, df2, on='Emp_ID', how='right')
print("\nThis is the right Join")
print(right_df)

outer_df = pd.merge(df1, df2, on='Emp_ID', how='outer')
print("\nThis is the outer Join")
print(outer_df)