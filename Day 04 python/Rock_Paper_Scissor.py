import random
Choose = ["Rock","Paper","Scissors"]


User_choice = int(input("What Do You Choose ? Type 1.for Rock 2.For Paper 3.For Scissor"))
Computer_choice= random.choice(Choose)
print(f"Computer Choose {Computer_choice}")

if User_choice == 1:
    print("You select rock")
    User_choice = "Rock"
elif User_choice == 2:
    print("You select paper")
    User_choice = "Paper"
elif User_choice == 3:
    print("You select scissor")
    User_choice = "scissor"
elif User_choice == 4:
    print("GameOver")
    sys.exit("Game Over... ")
else:
    print("Invalid Choice")

if User_choice == Computer_choice:
    print ("Draw Game...")
elif (User_choice == "Paper" and Computer_choice == "Rock") or (User_choice == "Rock" and Computer_choice == "Scissors") or (User_choice == "Scissors" and Computer_choice == "Paper"):
    print("You Win...")
else:
    print("Computer Win...")