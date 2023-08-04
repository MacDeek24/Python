print("Welcome To treasure Island")
print("Your Mission Is To Find The Treasure ")

LR= input("You're At A Cross Road . where Do you Want To Go? Type 'Left'  or 'Right'").lower()
if (LR =="left"):
    WS=input("You Come To A Lake. There is a island in the middle of The lake. Type 'Wait' to wait for a boat. Type 'Swim' TO Swim Across ").lower()
    if (WS == "wait"):
        RBY=input("You Arrive at The Island Unharmed. There Is A House With 3 doors. One Red One Yellow and One Blue. which Colour Do You Choose?").lower()
        if(RBY == "yellow"):
            print ("Congratulations You Found the TREASURE!!!")
        else:
            print("Game Over")
    else:
        print("Game Over")
else:
        print("Game Over")