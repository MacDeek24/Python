import pandas
import random

current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("french_words.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

# print(to_learn)

def next_card():
    global current_card
    current_card = random.choice(to_learn)
    print("French:", current_card["French"])


def is_known():
    to_learn.remove(current_card)
    print("Removed from learning list.")
    next_card()


while to_learn:
    next_card()
    input("Press Enter to reveal the English translation...")
    print("English:", current_card["English"])
    response = input("Did you know this word? (yes/no): ").strip().lower()
    if response == "yes":
        is_known()

print("You have learned all the words!")
