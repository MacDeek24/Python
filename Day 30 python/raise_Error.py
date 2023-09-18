height = float(input("Height : "))
weight = int(input("weight :"))
if height > 3:
    raise ValueError("Human Height should not be over 3 meter")
bmi = weight/ height ** 2
print(bmi)