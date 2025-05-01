import pandas as pd

# Expense categories
categories = ['Groceries', 'Utilities', 'Rent', 'Transportation', 'Entertainment']

# Monthly expense data in USD
expenses = [500, 200, 1200, 300, 150]

# Create a Pandas Series
expense_series = pd.Series(expenses, index=categories)

# Display the Series
print("Monthly Household Expenses:\n")
print(expense_series)

# Total monthly expense
total = expense_series.sum()
print("\nTotal Monthly Expense: $", total)

# Category with highest expense
max_category = expense_series.idxmax()
print("\nCategory with Highest Expense:", max_category)

# Category with lowest expense
min_category = expense_series.idxmin()
print("\nCategory with Lowest Expense:", min_category)

# Average expense per category
average = expense_series.mean()
print("\nAverage Expense per Category: $", round(average, 2))
