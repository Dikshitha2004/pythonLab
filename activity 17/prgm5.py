import pandas as pd
# Months of the year
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
          'September', 'October', 'November', 'December']

# Monthly advertising revenue data
revenue = [5000, 5200, 4800, 5400, 5600, 5800, 6100, 5900, 6200, 6500, 7000, 6900]

# Create Pandas Series
revenue_series = pd.Series(revenue, index=months)

# Display revenue data
print("Monthly Advertising Revenue (USD):\n", revenue_series)

# Total annual revenue
print("\nTotal Annual Revenue: $", revenue_series.sum())

# Highest and lowest revenue months
print("Highest Revenue Month:", revenue_series.idxmax(), "($", revenue_series.max(), ")")
print("Lowest Revenue Month:", revenue_series.idxmin(), "($", revenue_series.min(), ")")

# Average monthly revenue
print("Average Monthly Revenue: $", round(revenue_series.mean(), 2))
