from gameData import data
from art import vs
import random

def Compare(x, y):
    return x['follower_count'] > y['follower_count']


def higherOrlower(higher=0, x=0):
    if x == 0:
        from art import logo
        print(logo)
        score = 0
        choice1 = random.choice(data)
    else:
        score = x
        choice1 = higher
        print(f"That's right! Your current score is: {score}")

    choice2 = random.choice(data)
    while choice1 == choice2:
        choice2 = random.choice(data)
    options = {
        "op1": choice1,
        "op2": choice2
    }

    count = 0
    for x in options:
        name = options[x]['name']
        description = options[x]['description']
        country = options[x]['country']
        if count == 1:
            print(vs)
            print(f"Against B: {name}, a {description} from {country}.")
        else:
            print(f"Compare A: {name}, a {description} from {country}.")
        count += 1

    userChoice = input("Who has more followers on Instagram? 'A' or 'B': ").lower()

    if userChoice == 'a' and Compare(choice1, choice2):
        score += 1
        higherOrlower(options["op1"], score)
    elif userChoice == 'b' and not Compare(choice1, choice2):
        score += 1
        higherOrlower(options["op2"], score)
    else:
        print(f"Sorry that's wrong!, You're final score: {score}")
        again = input("Do you want to play again? 'y' or 'n': ").lower()
        if again == 'y':
            higherOrlower()
        else:
            return "GoodBye :). "



higherOrlower()
