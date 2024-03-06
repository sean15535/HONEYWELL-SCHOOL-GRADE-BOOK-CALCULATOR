grade={ }
print("Welcome to Honeywell Group of School Grade Calculator")
while True:
    print("1. Add Student Grade.\n2. Remove Student Grade.\n3 View Student Grades.\n4. Calculate Average Grade.\n5. Exit ")
    response = int(input(">>> "))
    if response == 1:
        student_name = str(input("Enter Student Name: "))
        if student_name in gradebook:
            print(f"Warning: {student_name} already exists in the gradebook. Overwriting grade.")
        student_grade = float(input("Enter Student Grade: "))
        grade[student_name]=student_grade
        print(f"{student_name} with {student_grade} has been added to the Gradebook")
    elif response == 2:
        if not grade:
            print("Gradebook is empty")
        else:
            reply = str(input("Enter Student Name to Remove: "))
            if reply 
            grade.pop[reply]
            print(f"{reply} has been removed from the GradeBook")
        

