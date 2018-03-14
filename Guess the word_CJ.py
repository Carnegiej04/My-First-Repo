import random

words = ["Saints","Basketball","Video Games","School",]

hint1 = ["Football Team","A Sport","Play on the weekends","I dont like going here"]

hint2 = ["My favorite football team", "NBA", "Fortnite", "Math, Science, Spanish,etc."]

number = random.randint(0,3)

secretword = words[number]

guess = ""

counter = 1

while True:
    print("Guess the secret word")
    print("Type 'hint1', 'hint2'")
    guess = input ()

    if guess == secretword:
        print ("You Win! It took you" + str(counter) + "guesses.")
        break

    elif guess == "hint1":
        print( hint1[number] )
    elif guess == "hint1":
        print( hint2[number] )

    elif guess == "first letter":
        print(secretword[0])
    
    elif guess == "last letter":
        print(secretword[-1])

    elif guess == "give up":
        print("The word was " +secretword)
        break

    else:
        counter +=1
