import random
import string
import json

# Password Generator
def generate_password():
    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    return password

# Save Password
def save_password(website, email, password):
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        data = {}

    data[website] = {"email": email, "password": password}

    with open("data.json", "w") as data_file:
        json.dump(data, data_file, indent=4)

# Find Password
def find_password(website):
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            if website in data:
                return data[website]["password"]
    except FileNotFoundError:
        return None

# Main Program
while True:
    print("Options:")
    print("1. Generate Password")
    print("2. Find Password")
    print("3. Quit")
    user_choice = input("Select an option: ")

    if user_choice == "1":
        website = input("Enter website: ")
        email = input("Enter email/username: ")
        password = generate_password()
        print(f"Generated Password: {password}")
        save_password(website, email, password)
    elif user_choice == "2":
        website = input("Enter website to find password: ")
        found_password = find_password(website)
        if found_password:
            print(f"Password for {website}: {found_password}")
        else:
            print(f"No password found for {website}")
    elif user_choice == "3":
        break
    else:
        print("Invalid option. Please choose a valid option.")
