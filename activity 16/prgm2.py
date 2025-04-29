import matplotlib.pyplot as plt
# Data
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
city1_temp = [22, 24, 23, 25, 26, 28, 27]
city2_temp = [18, 19, 20, 22, 23, 24, 25]

# Line Chart
plt.plot(days, city1_temp, label='City A', marker='o')
plt.plot(days, city2_temp, label='City B', marker='s')
plt.title('Temperature Comparison Between Two Cities')
plt.xlabel('Days')
plt.ylabel('Temperature (°C)')
plt.legend()
plt.grid(True)
plt.show()
