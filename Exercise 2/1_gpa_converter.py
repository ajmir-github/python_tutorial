# A+ 95-100
# A 90-95
# B+ 85-90
# B 80-85
# C 60-80

# GPA scale = percentage/20 - 1















percentage = int(input("Enter your percentage: "))
gpa = percentage/20 - 1

letter_grade = ""

if percentage >= 95:
 letter_grade = "A+"
elif percentage >= 90:
 letter_grade = "A"
elif percentage >= 85:
 letter_grade = "B+"
elif percentage >= 80:
 letter_grade = "B"
elif percentage >= 60:
 letter_grade = "C"
else:
 letter_grade = "Failed!"


print("GPA: "+str(gpa))
print("Grade: "+letter_grade)