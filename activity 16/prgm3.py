import matplotlib.pyplot as plt
import numpy as np

# Example Data
visitors = np.random.normal(loc=300, scale=50, size=100)

# Histogram
plt.hist(visitors, bins=10, color='skyblue', edgecolor='black')
plt.title('Distribution of Daily Website Visitors')
plt.xlabel('Number of Visitors')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
