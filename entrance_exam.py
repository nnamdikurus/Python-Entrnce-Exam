student_name = input("Enter student's name\n")

student_grade = float(input("Enter student's GPA\n"))

if student_grade <= 0.9:
    print(f"Sorry {student_name}, you have failed!!!")


elif student_grade <= 1.49:
    print(f"Hmmm {student_name}, you scraped through with a GPA of {student_grade} which is a PASS")

elif student_grade <=2.49:
    print(f"Goodluck {student_name}, you graduated with a GPA of {student_grade} which is a Third Class")

elif student_grade <= 3.49:
    print(f"Weldone {student_name}, you graduated with a GPA of {student_grade} which is a Second class Lower")

elif student_grade <= 4.49:
    print(f"Good job {student_name}, you graduated with a GPA of {student_grade} which is a Second Class Upper")

elif student_grade <= 5.0:
    print(f"Congratulations {student_name}!!! You graduated with a GPA of {student_grade} which is a FIRST CLASS")

else:
    print("Sorry!!! You entered an invalid score")





