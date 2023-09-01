# Game Guessing The Number
from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_ans(user_guess, comp_num, turn):
    if (user_guess < comp_num):
        print ("Too Low")
        return turn -1
    elif(user_guess > comp_num):
        print("Too high")
        return turn -1
    else:
        print(f"You got it ! The answer was {comp_num}")


def set_difficulty():
    level= input("Choose a difficulty type 'easy' or 'hard' :")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
def game():
    comp_num= randint(1,100)
    # print(comp_num)
    turn= set_difficulty()
    
    user_guess =0
    while user_guess != comp_num:
        print(f"You have {turn} attempts remaining to guess the number.")
        user_guess = int(input("Guess The Number :"))
        turn=check_ans(user_guess , comp_num , turn)
        if turn == 0:
            print("You've run out of guesses, you loes.")
            return

game()
