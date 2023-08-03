a=int(input("Enter The Total bill"))
b=int(input("What percentage tip would you like to give ? 10 or 15 or 20 "))
c = int(input("How many people to split the bill ?"))

d = a*b/100

e = (a+d)/c
print(f"Each person should pay {e} rupees")