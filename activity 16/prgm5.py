import matplotlib.pyplot as plt
import numpy as np
# Data
days = list(range(1, 31))
product1_sales = np.random.randint(50, 150, size=30)
product2_sales = np.random.randint(40, 140, size=30)

# Line Chart
plt.plot(days, product1_sales, label='Product 1', marker='o')
plt.plot(days, product2_sales, label='Product 2', marker='x')
plt.title('Sales Comparison of Two Products Over a Month')
plt.xlabel('Day of the Month')
plt.ylabel('Sales Units')
plt.legend()
plt.grid(True)
plt.show()
