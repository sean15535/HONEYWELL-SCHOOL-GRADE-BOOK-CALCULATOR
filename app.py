grade={ }
print("Welcome to Honeywell Group of School Grade Calculator")
while True:
    print("1. Add Student Grade.\n2. Remove Student Grade.\n3 View Student Grades.\n4. Calculate Average Grade.\n5. Exit ")
    response = int(input(">>> "))
    if response == 1:
        student_name = str(input("Enter Student Name: "))
        student_grade = float(input("Enter Student Grade: "))
        grade[student_name]=student_grade
        print(f"{student_name} with {student_grade} has been added to the Gradebook")
    elif response == 2:
