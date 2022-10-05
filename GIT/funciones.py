from email import feedparser
import random

def guess(x):
    randomNumber = random.randint(1, x)
    userNumber = 0
    while userNumber != randomNumber:
        userNumber = int(input(f"Guess a number between 1 and {x} "))
        if  userNumber > randomNumber:
            print("Too high")
        elif userNumber < randomNumber:
             print("Too low")
    print("Yey, there you go!!")


def computerGuess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback= input(print(f"Computer says {guess}, Correct (c), Too high (h), Too low (l)"))
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
    print(f"Computer guessed right, your number is {guess}")

computerGuess(10)