import matplotlib.pyplot as plt
height = [150, 160, 170, 180, 190]
weight = [50, 60, 65, 75, 85]

plt.scatter(height, weight, color='red')
plt.title("Height vs Weight")
plt.xlabel("Height (cm)")
plt.ylabel("Weight (kg)")
plt.show()
