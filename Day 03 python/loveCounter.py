name1 = input("Enter Your Name : ")
name2 = input("Enter their Name : ")

Comb_str= name1 + name2
LoerCaseString = Comb_str.lower()

t = LoerCaseString.count("t")
r = LoerCaseString.count("r")
u = LoerCaseString.count("u")
e = LoerCaseString.count("e")

true = t + r + u +e

l = LoerCaseString.count("l")
o = LoerCaseString.count("o")
v = LoerCaseString.count("v")
e = LoerCaseString.count("e")

love = l+o+v+e

Love_Score = int(str(true) +str(love))

if (Love_Score <10) or (Love_Score >90):
    print (f"Your Love Score is {Love_Score} , You Go Together like Cock And Mentos")
elif(Love_Score >=40) and (Love_Score <=50):
    print (f"Your Love Score is {Love_Score} , You are alright together.")
else:
    print(f"Your Score is {Love_Score}")


print(Love_Score)