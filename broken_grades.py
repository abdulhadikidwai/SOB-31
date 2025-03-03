# Calculating Grades (ok, let me think about this one)

# Write a program that will average 3 numeric exam grades, return an average test score, a corresponding letter grade, and a message stating whether the student is passing.

# Average	Grade
# 90+	A
# 80-89	B
# 70-79	C
# 60-69	D
# 0-59	F

# Exams: 89, 90, 90
# Average: 90
# Grade: A
# Student is passing.

# Exams: 50, 51, 0
# Average: 33
# Grade: F
# Student iis failing.

exam_one = int(input("Input exam grade one: "))

exam_two = int(input("Input exam grade two: ")) # added int

exam_three = int(input("Input exam grade three: ")) #Changed to int and 3 to three

grades = [exam_one, exam_two, exam_three] #Added missing commas
sum = 0
for grade in grades: # changed grade to grades
  sum = sum + grade

avg = sum / len(grades) #Fixed variable name to grades

if avg >= 90:
    letter_grade = "A"
elif avg >= 80: # Added missing colon
    letter_grade = "B"
elif avg >= 70:  # Line 16 (Fixed comparison operator and missing colon)
    letter_grade = "C"
elif avg >= 60:  # Line 18 (Fixed comparison operator and missing colon)
    letter_grade = "D"
else: # Fixed logical error
    letter_grade = "F"

for grade in grades:
    print("Exam: " + str(grade)) #Corrected to grades

    print("Average: " + str(avg))

    print("Grade: " + letter_grade)

if letter_grade == "F": # changed - to _ and is to ==
    print("Student is failing.") # Added brackets
else:
    print("Student is passing.") # Added brackets

# By- Abdul Hadi Kidwai (M00990950)