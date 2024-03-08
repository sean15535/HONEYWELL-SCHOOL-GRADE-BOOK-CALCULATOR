grade = {}

def grade_calculator():
    if not grade:
        print("Grade Book is empty")
        return

    total_grades = sum(grade.values())
    average_grade = total_grades / len(grade)
    print(f"Average Grade: {average_grade:.2f}")

def greetings():
    print("1. Add Student Grade.")
    print("2. Remove Student Grade.")
    print("3. View All Students and Grades.")
    print("4. Calculate Average Grade.")
    print("5. Exit")

def add_student():
    student_name = input("Enter Student Name: ").capitalize()
    if student_name in grade:
        print(f"Warning: {student_name} already exists in the gradebook. Overwriting grade.")
    try:
        student_grade = float(input("Enter Student Grade: "))
    except ValueError:
        print("Invalid grade input. Please enter a number.")
        return
    grade[student_name] = student_grade
    print(f"{student_name} with grade {student_grade} has been added to the Gradebook")


def remove_student_grade():
    if not grade:
        print("Gradebook is empty")
        return
    student_name = str(input("Enter Student Name to Remove: ")).capitalize()
    if student_name in grade:
        grade.pop(student_name) 
        print(f"{student_name}'s grade has been removed from the gradebook.")
    else:
        print(f"{student_name} does not exist in the gradebook.")

def students_grade():
    if not grade:
        print("Grade Book is empty")
        return
    print("Honeywell Grade Book")
    for student_name, grades in grade.items():
        print(f"{student_name}, {grades}")
