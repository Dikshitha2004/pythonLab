import matplotlib.pyplot as plt
subjects = ["Math", "Science", "English", "History", "Art"]
marks = [88, 76, 90, 70, 85]

plt.bar(subjects, marks, color='skyblue')
plt.title("Marks in 5 Subjects")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()
