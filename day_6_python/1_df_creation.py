import pandas as pd
import numpy as np
# We are using the pd.series coz we wanted to explecitly declare the datatype of the veriables

df = pd.DataFrame({
    "emp_id": pd.Series(
        [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
        dtype="int64"
    ),
             
    "employee_name": pd.Series(
        ["Alice", "Bob", "Charlie", "David", "Eva",
         "Frank", "Grace", "Henry", "Ivy", "Jack"],
        dtype="string"
    ),

    "salary": pd.Series(
        [55000.50, 62000.75, 71000.25, 48000.00, 68000.80,
         75000.90, 53000.40, 61000.60, 72000.10, 66000.55],
        dtype="float64"
    ),

    "is_active": pd.Series(
        [True, False, True, True, False,
         True, True, False, True, True],
        dtype="bool"
    ),

    "joining_date": pd.to_datetime([
        "2023-01-15",
        "2022-06-10",
        "2024-03-20",
        "2021-11-05",
        "2020-08-18",
        "2023-09-25",
        "2022-12-30",
        "2021-04-14",
        "2024-01-08",
        "2023-05-12"
    ]),

    "department": pd.Series(
        ["HR", "IT", "Finance", "Sales", "Marketing",
         "IT", "HR", "Finance", "Sales", "Marketing"],
        dtype="category"
    ),

    "experience_years": pd.Series(
        [5, 8, 3, 10, 7, 4, 6, 9, 2, 5],
        dtype="int32"
    ),

    "bonus": pd.Series(
        [5000.25, np.nan, 7000.50, 4500.00, 6500.75,
         8000.00, np.nan, 7200.40, 3900.00, 5800.60],
        dtype="float32"
    ),

    "work_duration": pd.to_timedelta([
        "1 days",
        "2 days",
        "12 hours",
        "3 days",
        "18 hours",
        "4 days",
        "2 days 6 hours",
        "1 days 12 hours",
        "20 hours",
        "5 days"
    ]),

    "remarks": pd.Series(
        ["Good", "Excellent", "Average", "Very Good", "Good",
         "Excellent", "Average", "Good", "Very Good", "Excellent"],
        dtype="object"
    )
})

print(df)

print("\nData Types:")
print(df.dtypes)

print("\nDataFrame Info:")
df.info()


# Save to CSV
df.to_csv("employees.csv", index=False)

# Save to Excel
df.to_excel("employees.xlsx", index=False)

print("Files saved successfully!")
