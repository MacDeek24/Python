# who Give A trip choose A Random Through
import random
Str_split=input("Enter The All Group Members Name")
OP = Str_split.split(" ")
print(OP)
Numitem=len(OP)
Random_Choice=random.randint(0,Numitem - 1)
print(OP[Random_Choice] + "Today trip ")
