import requests
import html  # Import the html module to unescape HTML entities

parameters = {
    "amount": 10,
    "type": "boolean"
}

response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()
question_data = data["results"]


def create_question_bank(question_data):
    question_bank = []
    for question in question_data:
        question_text = html.unescape(question["question"])  # Unescape HTML entities
        question_answer = question["correct_answer"]
        question_bank.append((question_text, question_answer))
    return question_bank


def still_has_questions(question_number, question_list):
    return question_number < len(question_list)


def next_question(question_number, question_list, score):
    current_question = question_list[question_number]
    question_number += 1
    user_answer = input(f"Q.{question_number}: {current_question[0]} (True/False): ")
    score = check_answer(user_answer, current_question[1], score)
    return question_number, score


def check_answer(user_answer, correct_answer, score):
    if user_answer.lower() == correct_answer.lower():
        score += 1
        print("You got it right!")
    else:
        print("That's wrong.")

    print(f"Your current score is: {score}/{question_number+1}")
    print("\n")
    return score


question_bank = create_question_bank(question_data)
question_number = 0
score = 0

while still_has_questions(question_number, question_bank):
    question_number, score = next_question(question_number, question_bank, score)

print("You've completed the quiz")
print(f"Your final score was: {score}/{len(question_bank)}")
