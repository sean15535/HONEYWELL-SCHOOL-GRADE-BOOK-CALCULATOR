from functions import grade_calculator, greetings, add_student, remove_student_grade, students_grade

print("Welcome to Honeywell Group of School Grade Calculator")

while True:
    greetings()
    response = input(">>> ")

    if response == '1':
        add_student()
    elif response == '2':
        remove_student_grade()
    elif response == '3':
        students_grade()
    elif response == '4':
        grade_calculator()
    elif response == '5':
        print("Exiting App")
        break
    else:
        print("Invalid Command, Try again")
