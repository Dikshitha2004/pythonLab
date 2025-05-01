import pandas as pd

# Creating the DataFrame
data = {
    'Employee': ['John', 'Alice', 'Bob', 'Emma'],
    'Department': ['IT', 'HR', 'Finance', 'IT'],
    'Salary': [60000, 55000, 70000, 72000],
    'Age': [30, 28, 35, 32]
}

df = pd.DataFrame(data)

# 1. Display the first two rows
print(df.head(2))

# 2. Add new column "Experience"
df["Experience"] = [5, 3, 7, 6]

# 3. Find the average salary
avg_salary = df["Salary"].mean()
print("Average Salary:", avg_salary)
