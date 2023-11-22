# Derek Wood

# 2B

# November 22, 2023

import random
n = random.randint(1,99)
guess = int(input("Guess an interger from 1 to 99:"))
while True:
    if guess < n:
        print("guess is low")
        guess = int(input("Guess an interger from 1 to 99:"))
    elif guess > n:
        print("guess is high")
        guess = int(input("Guess an interger from 1 to 99:"))
    else:
        print("you guessed it right! Bye!")
        break