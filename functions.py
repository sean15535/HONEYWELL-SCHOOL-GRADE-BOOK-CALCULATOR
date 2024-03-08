grade = {}

def grade_calculator():
    total_grades = sum(grade.values())
    average_grade = total_grades / len(grade)
    return f"Average Grade: {average_grade}"

def greetings():
    print("1. Add Student Grade.")
    print("2. Remove Student Grade.")
    print("3. View All Students and Grades.")
    print("4. Calculate Average Grade.")
    print("5. Exit")

def add_student():
    student_name = str(input("Enter Student Name: "))
    if student_name in grade:
        print(f"Warning: {student_name} already exists in the gradebook. Overwriting grade.")
        student_grade = float(input("Enter Student Grade: "))
        grade[student_name] = student_grade
    return f"{student_name} with grade {student_grade} has been added to the Gradebook"