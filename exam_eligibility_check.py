# 1) Ask the student if they had a medical cause and store the answer in `medical_cause`.

# (Also clean the input so it becomes either 'Y' or 'N'.)

# 2) If `medical_cause` is 'Y':

# - Print that the student is allowed to attend the exam.

# 3) Otherwise (medical_cause is 'N'):

# a) Ask for the student’s attendance percentage and store it in `atten`.

# b) If `atten` is 75 or more:

# - Print "Allowed"

# c) Else:

# - Print "Not allowed"

medical_clause=input("if you had a medical cause(y or n):")
if medical_clause=="y":
    print("the student is allowed to attend the exam")
else:
    print("the student is not allowed to attend the exam")
    atten=int(input("enter your attendance:"))
    if atten >=75:

       print("Allowed")
    else:
       print("not allowed")

