Y=int(input("Enter a Year : "))
if(Y%4==0) and (Y%100 != 0):
    print(f"{Y} is a Leap year")
else:
    print(f"{Y} is Not a Leap Year")