# find an avg of student's mark
Stu_height = input("input a list of student height ").split()
for n in range(0, len(Stu_height)):
    Stu_height[n] = int(Stu_height[n])
print(Stu_height)

total_height=0
for height in Stu_height:
   
    total_height += height
print(total_height)

Num_Stu =0
for Stu in Stu_height:
    Num_Stu +=1
print(Num_Stu)

avg_height= total_height/Num_Stu
print(avg_height)

# total_height= sum(Stu_height)
# Num_Stu = len(Stu_height)

# avg_height= total_height/Num_Stu
# print(avg_height)