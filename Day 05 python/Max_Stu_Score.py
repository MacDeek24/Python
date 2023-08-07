Stu_Score = input("input a list of student Score ").split()
for n in range(0, len(Stu_Score)):
    Stu_Score[n] = int(Stu_Score[n])
print(Stu_Score)

High_Score= 0
for score in Stu_Score:
    if score > High_Score:
        High_Score = score
print(f"The high score is : {High_Score}")  

a="lad"
b=int(a)
print(b)