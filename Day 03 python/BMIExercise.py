h = float(input("enter your height in m: "))
w = int(input("enter your weight in kg: "))

bmi= w/h**2
print(bmi)

if (bmi<= 18.5):
    print("You Are under weight")
elif (bmi > 18.5 and bmi <= 25):
    print ("you are normal weight")
elif (bmi > 25 and bmi <= 30):
    print ("you are Over weight")
elif (bmi > 30 and bmi <= 35):
    print ("you are Obese")
else:
    print ("you are Obese")