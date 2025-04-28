import matplotlib.pyplot as plt
import numpy as np

ages = np.random.randint(18, 70, 100)  # Generating 100 random ages between 18 and 70

plt.hist(ages, bins=10, color='purple', edgecolor='black')
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Number of People")
plt.show()
