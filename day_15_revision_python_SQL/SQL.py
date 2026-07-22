# ==========================================================
# SQL BASICS
# ==========================================================

# Select all the data from the table
# SELECT * FROM employees;

# ==========================================================
# CREATE TABLE
# ==========================================================

# CREATE TABLE is used to create a new table in the database.
# While creating a table, we define:
# - Column names
# - Data types
# - Constraints (if required)


# ==========================================================
# Example 1 : Simple Table
# ==========================================================

# Create a simple employees table.

"""
CREATE TABLE employees (
    emp_id INT,
    emp_name VARCHAR(100),
    salary DECIMAL(10,2),
    gender VARCHAR(10)
);
"""

# Explanation:
# emp_id           -> Stores employee id
# emp_name         -> Stores employee name (maximum 100 characters)
# salary           -> Stores salary with 2 digits after decimal
# gender           -> Stores employee gender


# ==========================================================
# Example 2 : Table with Constraints
# ==========================================================

# Here we are applying different constraints while creating
# the table.

"""
CREATE TABLE employees (

    emp_id INT PRIMARY KEY,
    -- Every employee must have a unique id.
    -- NULL values are not allowed.

    emp_name VARCHAR(100) NOT NULL,
    -- Employee name cannot be empty.

    email VARCHAR(100) UNIQUE,
    -- Every employee must have a different email.

    age INT CHECK(age >= 18),
    -- Age must be 18 or greater.

    salary DECIMAL(10,2) DEFAULT 25000,
    -- If salary is not provided,
    -- SQL automatically stores 25000.

    gender VARCHAR(10)
);
"""


# ==========================================================
# PRIMARY KEY
# ==========================================================

# PRIMARY KEY
# - Uniquely identifies every row.
# - Cannot contain NULL values.
# - Duplicate values are not allowed.


# ==========================================================
# FOREIGN KEY
# ==========================================================

# A FOREIGN KEY creates a relationship between two tables.
# It ensures that the value exists in another table.


# ==========================================================
# Example 3 : Parent Table
# ==========================================================

"""
CREATE TABLE departments (

    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(100) NOT NULL

);
"""

# This table stores department information.
# dept_id will be referenced by another table.


# ==========================================================
# Example 4 : Child Table (Using Foreign Key)
# ==========================================================

"""
CREATE TABLE employees (

    emp_id INT PRIMARY KEY,

    emp_name VARCHAR(100) NOT NULL,

    salary DECIMAL(10,2),

    dept_id INT,

    FOREIGN KEY (dept_id)
    REFERENCES departments(dept_id)

);
"""

# Explanation:

# dept_id in employees is a FOREIGN KEY.

# REFERENCES departments(dept_id)
# means:
# The value entered in employees.dept_id
# must already exist in departments.dept_id.

# Example:

# departments table

# dept_id    dept_name
# --------------------
# 1          HR
# 2          IT
# 3          Sales

# Valid Inserts

# emp_id   emp_name   dept_id
# ---------------------------
# 101      Rahul      1
# 102      Amit       2

# Invalid Insert

# emp_id   emp_name   dept_id
# ---------------------------
# 103      Neha       10

# Because department id 10 does not exist
# in the departments table.


# ==========================================================
# Why do we use Foreign Keys?
# ==========================================================

# They help maintain referential integrity.

# Without a foreign key:

# Employee can belong to department 500
# even if department 500 doesn't exist.

# With a foreign key:

# SQL will throw an error if the department
# does not exist.


# ==========================================================
# Quick Revision
# ==========================================================

# CREATE TABLE
# -> Creates a new table.

# PRIMARY KEY
# -> Unique + Not NULL.

# FOREIGN KEY
# -> Links one table with another.

# NOT NULL
# -> Value cannot be empty.

# UNIQUE
# -> Duplicate values are not allowed.

# CHECK
# -> Restricts values based on a condition.

# DEFAULT
# -> Uses a default value when no value is provided.

# ==========================================================
# CONSTRAINTS
# ==========================================================

# Constraints are a set of rules applied to table columns
# to maintain the accuracy, integrity, and validity of the data.
#
# Common Constraints:

# - PRIMARY KEY
#   -> Uniquely identifies each row in a table.
#   Example:
#   id INT PRIMARY KEY

# - FOREIGN KEY
#   -> Creates a relationship between two tables.
#   Example:
#   dept_id INT,
#   FOREIGN KEY (dept_id) REFERENCES department(id)

# - NOT NULL
#   -> Ensures a column cannot have NULL values.
#   Example:
#   name VARCHAR(100) NOT NULL

# - UNIQUE
#   -> Ensures all values in the column are unique.
#   Example:
#   email VARCHAR(100) UNIQUE

# - CHECK
#   -> Allows only values that satisfy a condition.
#   Example:
#   age INT CHECK (age >= 18)

# - DEFAULT
#   -> Assigns a default value if none is provided.
#   Example:
#   country VARCHAR(50) DEFAULT 'India'

# ==========================================================
# SELECT QUERIES
# ==========================================================

# Select employee name and salary of female employees
# whose salary is less than 70000.
# Display the result in descending order of salary
# and return only the second highest salary.

# SELECT emp_name, salary
# FROM employees
# WHERE gender = 'Female' AND salary < 70000
# ORDER BY salary DESC
# LIMIT 1 OFFSET 1;


# Select employees whose salary is between 50000 and 80000

# SELECT *
# FROM employees
# WHERE salary BETWEEN 50000 AND 80000;


# ==========================================================
# UPDATE QUERY
# ==========================================================

# UPDATE is used to modify the existing data (values)
# in one or more rows of a table.

# Syntax:
# UPDATE table_name
# SET column_name = value
# WHERE condition;

# Example:
# UPDATE employees
# SET salary = 80000
# WHERE emp_id = 101;

# ==========================================================
# ALTER TABLE
# ==========================================================

# ALTER is used to modify the structure (schema) of an
# existing table. It does NOT update the data itself.

# Common operations:
# - Add a new column
# - Drop an existing column
# - Rename a column
# - Change a column's data type
# - Add or remove constraints

# Examples:

# Add a column
# ALTER TABLE employees
# ADD age INT;

# Drop a column
# ALTER TABLE employees
# DROP COLUMN age;

# Rename a column
# ALTER TABLE employees
# RENAME COLUMN emp_name TO employee_name;

# Modify a column's data type
# ALTER TABLE employees
# MODIFY salary DECIMAL(10,2);

# ==========================================================
# DELETE QUERY
# ==========================================================

# Delete the user whose id is 1

# DELETE FROM user
# WHERE id = 1;


# Delete all users whose gender is 'Other'

# DELETE FROM user
# WHERE gender = 'Other';


# ==========================================================
# GROUP BY
# ==========================================================

# Calculate the total salary department-wise

# SELECT SUM(salary) AS total_salary
# FROM employee_table
# GROUP BY dept_column;


# Calculate the average salary gender-wise

# SELECT AVG(salary) AS avg_salary
# FROM employee
# GROUP BY gender;


# Find the minimum and maximum salary gender-wise

# SELECT
#     MIN(salary) AS minimum_salary,
#     MAX(salary) AS maximum_salary
# FROM table1
# GROUP BY gender;


# ==========================================================
# COMMIT AND ROLLBACK
# ==========================================================

# Disable Auto Commit
#
# SET autocommit = 0;
#
# When auto-commit is disabled, changes made using
# INSERT, UPDATE, or DELETE are not saved permanently
# until you execute:
#
# COMMIT;
#
# Once COMMIT is executed, the changes become permanent.


# ==========================================================
# ROLLBACK
# ==========================================================

# ROLLBACK is used to undo changes made after the last COMMIT.
#
# It works like an "Undo" operation.
#
# Example:
# - You accidentally DELETE or UPDATE some records.
# - Before executing COMMIT, run:
#
# ROLLBACK;
#
# The table will return to its previous committed state.
#
# Note:
# ROLLBACK works only if the transaction has not been committed.
# If auto-commit is ON, each statement is committed immediately,
# and ROLLBACK cannot undo those changes.