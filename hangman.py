import time
import random
from nltk.corpus import words

#get a list of words using nltk
word_list = words.words()

#welcoming the user
name = input("\nWhat is your name? ")
print("\nHello " + name + ", Time to play hangman!\n")

#wait for 1 second 
time.sleep(2)
print("Start guessing...\n")

#here we set the secret
#word = "secret"
word = random.choice(word_list)
lengthOfWord = len(word)
print("The length of the word is : " + str(lengthOfWord) + " letters long")
time.sleep(3)


#creates an variable with an empty value
guesses = ''

#determine the number of turns
turns = 10

# Create a while loop

#check if the turns are more than zero
while turns > 0:         

    # make a counter that starts with zero
    failed = 0    
    
    print ("\n\n\t", end=" ")    
         
    # for every character in secret_word    
    for char in word:      

    # see if the character is in the players guess
        if char in guesses:    
    
        # print then out the character
            print (char, end=" ")    

        else:
    
        # if not found, print a dash
            print ("__", end=" ")     
       
        # and increase the failed counter with one
            failed += 1    

    # if failed is equal to zero

    # print You Won
    if failed == 0:        
        print ("\n\n\t*** You won ***")  

    # exit the script
        break              

    # ask the user go guess a character
    guess = input("\n\nGuess a character:") 

    # set the players guess to guesses
    contains = False
    for char in guesses:  
        if char == guess:
            contains = True    

    if not contains :
        guesses += guess                    

        # if the guess is not found in the secret word
        if guess not in word:  
 
            # turns counter decreases with 1 (now 9)
            turns -= 1        
 
            # print wrong
            print("\n\tIncorrect guess!\n")
 
            # if the turns are equal to zero
            if turns == 0:           
                # print "You Loose"
                print("\nYou are out of Guesses\n\n\tYou Loose")
                print("\nThe word was : " + word)
            else:
                print("You have " + str(turns) + " more guesses, please try again?\n")
        
        else:
            print("\n\tCorrect!")
    else:
        guess = input("\nYou have entered this before!\nPlease Guess another character : ") 

        