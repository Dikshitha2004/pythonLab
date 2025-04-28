import matplotlib.pyplot as plt
activities = ["Sleep", "Study", "Entertainment", "Exercise", "Others"]
hours = [8, 6, 4, 2, 4]

plt.pie(hours, labels=activities, autopct='%1.1f%%', startangle=90)
plt.title("Daily Activities")
plt.show()
