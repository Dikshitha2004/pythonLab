import matplotlib.pyplot as plt

# Data
regions = ['North', 'South', 'East', 'West']
population = [25, 30, 20, 25]

# Pie Chart
plt.figure(figsize=(6,6))
plt.pie(population, labels=regions, autopct='%1.1f%%', startangle=140)
plt.title('Population Distribution Among Regions')
plt.show()
