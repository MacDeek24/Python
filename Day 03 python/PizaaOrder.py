print("Welcome To Pizza order")
print("Small Pizza : 99 rs")
print("Medium Pizza : 199 rs")
print("Large Pizza : 399 rs")

S = input("what size pizza do you want ? S or M or L")
add_pepperoni=input("Do you want pepperoni ? Y or N")
Extra_Cheese=input("Do you want pepperoni ? Y or N")

Bill =0
if (S == "s") or (S == "S"):
    Bill += 99
elif (S == "M") or (S == "m"):
    Bill +=199
elif (S == "L") or (S == "l"):
    Bill +=399

if add_pepperoni == "Y" or add_pepperoni == "y":
    if (S == "s") or (S == "S"):
        Bill +=30
    else:
        Bill +=40

if (Extra_Cheese == "y") or (Extra_Cheese == "Y"):
    Bill+=25

print(f"Your Final Bill : {Bill} Rs")