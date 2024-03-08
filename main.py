from functions import grade_calculator, greetings, add_student, remove_student_grade
grade = {}

print("Welcome to Honeywell Group of School Grade Calculator")

while True:
    greetings()
    response = int(input(">>> "))

    if response == 1:
        add_student()
    elif response == 2:
        remove_student_grade()
    elif response == 3:
        if not grade:
            print("Grade Book is empty")
        else:
            print("Honeywell Grade Book")
            for student_name, grades in grade.items():
                print(f"{student_name}, {grades}")
    elif response == 4:
        if not grade:
            print("Grade Book is empty")
        else:
            grade_calculator()
    elif response == 5:
        print("Exiting App")
        break
    else:
        print("Invalid Command, Try again")
