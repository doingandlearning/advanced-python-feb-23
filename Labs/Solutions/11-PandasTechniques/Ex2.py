import pandas as pd

# load the datasets
employees = pd.read_csv("employees.csv")
employees_start = pd.read_csv("employees_start.csv")

merged = pd.merge(employees, employees_start)
print(merged)
