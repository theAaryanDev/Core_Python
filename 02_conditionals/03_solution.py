#My approach
marks = int(input("Please enter your marks out of 100: "))
if (marks < 60):
    print("F")
elif (marks < 70):
    print("D")
elif (marks < 80):
    print("C")
elif (marks < 90):
    print("B")
else:
    print("A")

#Sir approach
score = 185

if score >= 101:
    print("Please verify your grade again")
    exit()  #Learn this , exit() exit/closes/terminates the program here.

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print("Grade: ", grade)