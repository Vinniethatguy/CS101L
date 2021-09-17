person = input("Who are we calculating gardes for? ==> ")

lab = float(input("Enter the lab grades? ==> "))
if lab > 100:
    print("The lab value should have been 100 or less. It has been change to 100")
    lab = 100
if lab < 0:
    print('')
    lab = 0

exam = float(input("Enter the EXAMS grade? ==> "))
if exam > 100:
    print("The lab value should have been 100 or less. It has been changed to 100")
    exam = 100
if exam < 0:
    print("The exam value should have been 0 or more. It has been changed to 0")
    exam = 0

attend = float(input("Enter the Attendence grade? ==> "))
if attend > 100:
    print("The attendence valiue should have been 100 or less. It has been changed to 100")
    attend = 100
if attend < 0:
    print("The attendece value should have been 0 or more. It has been changed to 0")
    attend = 0
    
grade = float(lab * 0.7) + float(exam * 0.2) + float(attend * 0.1)

print(f"The weighted grade for {person} is {grade}")


if grade >= 90:
    print(f"{person} has a letter grade of A")
elif grade >= 80:
    print(f"{person} has a letter grade of B")
elif grade >= 70:
    print(f"{person} has a letter grade of C")
elif grade >= 60:
    print(f"{person} has a letter grade of D")
else:
    print(f"{person} has a letter grade of F")
