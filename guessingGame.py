import random

number = random.randint(1, 15)
guessCounter = 0

while guessCounter < 3:
    userGuess = int(input("Enter an integer from 1 to 15: "))
    guessCounter +=1
    print ("\nThis is your Guess : " + str(userGuess))
    
    if userGuess < number:
        print ("userGuess is low\n")
    elif userGuess > number:
        print ("userGuess is high\n")
    elif userGuess == number:
        break
    
if userGuess == number:
    guessCounter = str(guessCounter)
    print ("You Guessed it in : " + str(guessCounter))
    print("The secret number was : " + str(number))
    
if userGuess != number:
    number = str(number)
    print ("Sorry The secret number was : " + str(number))