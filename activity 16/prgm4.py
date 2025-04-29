import matplotlib.pyplot as plt
# Example Data
sales = [100, 200, 300, 400, 500]
profit = [20, 50, 80, 130, 180]

# Scatter Plot
plt.scatter(sales, profit, color='green')
plt.title('Sales vs Profit')
plt.xlabel('Sales ($)')
plt.ylabel('Profit ($)')
plt.grid(True)
plt.show()
