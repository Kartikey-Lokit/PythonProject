# Grade Calculator Important programe
# Write a program that calculate and display the letter grade for a given numerical score?
# For given numerical score (e.g.A,B,C,D,E)
# based on following grade

# A:90-100
# B:80-89
# C:70-79
# D:60-69
# E:0-59

# Logic Building
# 1-->User Input-->Score or mark-->int
# 2--o/p-->str-->A or B....

score = int(input("Enter your score\n"))
grade = "F"

if score >= 90 and score <= 100:
    grade = "A"
print("your grade is", "A")
elif score >= 80 and score <= 90:
grade = "B"
print("your grade is", "B")
elif score >= 70 and score <= 79:
grade = "C"
print("your grade is", "C")
elif score >= 60 and score <= 69:
grade = "D"
print("your grade is", "D")
elif score >= 0 and score <= 59:
grade = "E"
print("your grade is", "E")
else:
grade = "F"
print("your grade is", "F")
