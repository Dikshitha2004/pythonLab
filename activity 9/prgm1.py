students = []
def create_students():
    global students
    students = [
        ("Alice", 101, (85, 90, 78), "B"),
        ("Bob", 102, (76, 88, 91), "A"),
        ("Charlie", 103, (65, 70, 72), "C"),
    ]
def display_all_students():
    print("\nAll Students:")
    for s in students:
        print(f"Name: {s[0]}, Roll No: {s[1]}, Marks: {s[2]}, Grade: {s[3]}")
def add_student(name, roll, marks, grade):
    students.append((name, roll, marks, grade))
    print(f"\nStudent {name} added successfully.")
def search_student(roll):
    for s in students:
        if s[1] == roll:
            print(f"\nStudent Found: Name: {s[0]}, Roll No: {s[1]}, Marks: {s[2]}, Grade: {s[3]}")
            return
    print("\nStudent not found.")
def calculate_total_marks():
    print("\nTotal Marks for each student:")
    for s in students:
        total = sum(s[2])
        print(f"Roll No: {s[1]}, Name: {s[0]}, Total Marks: {total}")
def update_grade(roll, new_grade):
    global students
    updated = False
    for i in range(len(students)):
        if students[i][1] == roll:
            students[i] = (students[i][0], students[i][1], students[i][2], new_grade)
            print(f"\nUpdated grade for Roll No {roll} to {new_grade}.")
            updated = True
            break
    if not updated:
        print("\nStudent not found.")
def remove_student(roll):
    global students
    for i in range(len(students)):
        if students[i][1] == roll:
            print(f"\nRemoving student: {students[i][0]}, Roll No: {roll}")
            del students[i]
            return
    print("\nStudent not found.")

create_students()
display_all_students()
add_student("David", 104, (89, 85, 92), "A")
display_all_students()
search_student(102)
calculate_total_marks()
update_grade(101, "A")
remove_student(103)
display_all_students()
