student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades={}
"""Scores 91 - 100: Grade = "Outstanding"

Scores 81 - 90: Grade = "Exceeds Expectations"

Scores 71 - 80: Grade = "Acceptable"

Scores 70 or lower: Grade = "Fail"""

#TODO-2: Write your code below to add the grades to student_grades.👇
for item in student_scores:
  student_grades[item]=student_scores[item]
  if student_grades[item]<=70:
    student_grades[item]="Fail"
  elif student_scores[item]<=80:
    student_grades[item]="Acceptable"
  elif student_scores[item]<=90:
    student_grades[item]="Exceeds Expectations"
  elif student_scores[item]<=100:
    student_grades[item]="Outstanding"
      
      


# 🚨 Don't change the code below 👇
print(student_grades)

