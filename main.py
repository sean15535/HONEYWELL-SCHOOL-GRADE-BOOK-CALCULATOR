from functions import grade_calculator, greetings
grade = {}

print("Welcome to Honeywell Group of School Grade Calculator")

while True:
    greetings()
    response = int(input(">>> "))

    if response == 1:
        add_student()
    elif response == 2:
        if not grade:
            print("Gradebook is empty")
        else:
            student_name = str(input("Enter Student Name to Remove: "))
            if student_name in grade:
                grade.pop(student_name) 
                print(f"{student_name}'s grade has been removed from the gradebook.")
            else:
                print(f"{student_name} does not exist in the gradebook.")
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
