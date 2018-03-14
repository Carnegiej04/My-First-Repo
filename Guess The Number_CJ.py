import random
import time

number = random.randint(1,100)

Guess = 0

counter = 0

while True:
    counter += 1
    print("Guess my number between 1 and 100")
    guess = int ( input())

    if guess == number:
        print("You Win!")
        print("You Tried " + str(counter) + " guesses.")
        break
              
    elif guess < number:
              print("Too Low, Try again.")

    elif guess > number:
              print("Too High, try again.")
