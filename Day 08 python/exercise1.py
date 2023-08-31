import math
Test_h=int(input("Enter Wall height :"))
Test_W=int(input("Enter Wall width :"))
coverage = 5

def paint_calc(height, width):
    NumberOFCan=math.ceil((height*width)/coverage) 
    print(f"You'll Need {NumberOFCan} can of paint")

paint_calc(height= Test_h, width=Test_W)