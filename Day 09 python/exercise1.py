Student_Score ={
    "harry" : 81,
    "ronald":90 ,
    "ron" : 74,
    "neville":62, 
    } 

student_grades = {}

for student in Student_Score:
    score = Student_Score[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceed Expectation"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

print(student_grades)