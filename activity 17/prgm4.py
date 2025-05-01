import pandas as pd

# Months of the year
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
          'September', 'October', 'November', 'December']

# Monthly energy usage data
electricity_usage = [350, 320, 310, 330, 340, 370, 380, 360, 350, 330, 320, 330]
gas_usage = [20, 18, 16, 15, 12, 10, 8, 9, 12, 15, 17, 19]

# Create Pandas Series
electricity_series = pd.Series(electricity_usage, index=months)
gas_series = pd.Series(gas_usage, index=months)

# Display summary
print("Electricity Usage (kWh):\n", electricity_series)
print("\nGas Usage (therms):\n", gas_series)

# Total annual usage
print("\nTotal Annual Electricity Usage:", electricity_series.sum(), "kWh")
print("Total Annual Gas Usage:", gas_series.sum(), "therms")

# Peak usage month
print("\nMonth with Highest Electricity Usage:", electricity_series.idxmax())
print("Month with Highest Gas Usage:", gas_series.idxmax())

# Average usage
print("\nAverage Monthly Electricity Usage:", round(electricity_series.mean(), 2), "kWh")
print("Average Monthly Gas Usage:", round(gas_series.mean(), 2), "therms")
