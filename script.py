#Add unsuccessful guesses into the dictionary

import random
import json
import datetime

secret = random.randint(1, 30)
attempts = 0

with open("score_list.txt", "r") as score_file:
    score_list = json.loads(score_file.read())

for score_dict in score_list:
    print(str(score_dict["attempts"]) + " attempts, date: " + score_dict.get("date"))

print("First please fill in your name, before the game starts.")
name = input("Name: ")

guess_list = []

while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))
    attempts += 1

    if guess == secret:
        score_list.append({"attempts": attempts, "date": str(datetime.datetime.now()), "player": name, "secret number": secret, "wrong guesses": guess_list})
        with open("score_list.txt", "w") as score_file:
            score_file.write(json.dumps(score_list))
        print("You've guessed it - congratulations! It's number " + str(secret))
        print("Attempts needed: " + str(attempts))
        break
    elif guess > secret:
        guess_list.append(guess)
        print("Your guess is not correct... try something smaller")
    elif guess < secret:
        guess_list.append(guess)
        print("Your guess is not correct... try something bigger")

