import pandas as pd
# Creating a student DataFrame
student_data = {
    'Name': ['Alex', 'Ben', 'Cathy', 'Diana', 'Eva'],
    'Math': [85, 76, 92, 58, 89],
    'Science': [78, 88, 90, 60, 95],
    'English': [82, 74, 91, 67, 89]
}

students = pd.DataFrame(student_data)

# 1. Display students who scored more than 80 in Math
print("Students scoring more than 80 in Math:")
print(students[students['Math'] > 80])

# 2. Sort DataFrame by Science scores in descending order
sorted_students = students.sort_values(by='Science', ascending=False)
print("Sorted by Science (descending):")
print(sorted_students)

# 3. Find the student with the highest English score
highest_english = students.loc[students['English'].idxmax()]
print("Student with highest English score:")
print(highest_english)
