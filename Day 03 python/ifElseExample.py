H = int(input("Enter Your Height : "))
Bill = 0
if H > 120:
    print("You can go for roller coster")
    age=int(input("Enter your age : "))
    if(age<12):
        Bill=170
        print ("Please Pay 170 Rs")
    elif (age>=18):
        Bill=500
        print("please pay a 500 Rs")
    else:
        Bill=250
        print("Pleas pay 250 Rs")

    Want_Photo=input("Do you want photo taen ? Y or N")
    if (Want_Photo == "Y") or (Want_Photo == "y"):
        Bill2= Bill+50
        print(f"Total Bill : {Bill2}")
    elif(Want_Photo == "n") or (Want_Photo == "N"):
        print(f'Total bill is {Bill}')
    else:
        print('Invalid Input')
else:
    print("You can not go for roller coster")