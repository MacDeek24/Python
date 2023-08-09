# hangman game 

import random

stages =['''
        _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |     ./ \.
     |
    _|___ ''', '''
        _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / 
     |
    _|___''', '''
        _______
     |/      |
     |      (_)
     |      \|/
     |       
     |      
     |
    _|___''', '''
        _______
     |/      |
     |      (_)
     |      \|/
     |       
     |   
     |
    _|___''', '''
        _______
     |/      |
     |      (_)
     |       |
     |       
     |   
     |
    _|___''', '''
        _______
     |/      |
     |      (_)
     |      
     |       
     |   
     |
    _|___''', '''
        _______
     |/      |
     |      
     |      
     |       
     |   
     |
    _|___''']
word_list= ["apple", "anywhere","balloon", "king"]

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

live = 6

display = []

for _ in range(word_length):
    display += "_"
print (display)

end_of_game = False
while not end_of_game:
    guess = input("Guess a letter :").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter


    print(display)
    if guess not in chosen_word:
        print(f"you guessed {guess} , that's not in the word. you lose a life")
        live -=1
        if live ==0:
            end_of_game = True
            print ("You lose ")

    print(display)

    if "_" not in display:
        end_of_game=True
        print("You win")

    print(stages[live])