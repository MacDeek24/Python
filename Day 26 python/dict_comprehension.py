#Dictionary cpmprehension
import random
list = ["alex","Beth", "caroline", "Dave", "Eleanor", "Freddie"]
name = {student:random.randint(1,100) for student in list}

#only contain a passed student in new list
passed_student = {student: score for (student,score) in name.items() if score >=60}
print(name)
print(passed_student)
