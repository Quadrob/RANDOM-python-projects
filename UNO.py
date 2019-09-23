import random

#Funtion to return a random card from the pack
def getCard():
    
    #2 lists for the color of the cards and type of card
    cardColor = {0: 'Blue', 1: 'Green', 2: 'Red', 3: 'Yellow'}
    cardNum = {0:'2', 1:'3', 2:'4', 3:'5', 4:'6', 5:'7', 6:'8', 7:'9', 8:'Skip', 9:'Reverse Direction', 10:'Pick up 2', 11:'Pick up 4', 12:'Change Color', 13: '2', 14:'9', 15:'3', 16:'4', 17:'5', 18:'6', 19:'7', 20:'8'}    
    
    #if else statment to randomly build card and return it
    tempCardHolder = random.choice(cardNum)
    if (tempCardHolder == "Change Color" or tempCardHolder == "Pick up 4"):
        card = tempCardHolder    
    else:
        tempColorHolder = random.choice(cardColor)
        card = (tempColorHolder + " " + tempCardHolder)
        
    return (card)

#a function to determine if a card is legal to play
def isLegal(topCard, card):
    #if statment to see if you can play card
    if (card == "Change Color" or card == "Pick up 4" or card[0:3] == topCard[0:3] or card[-1:] == topCard[-1:]):
        return True
    else:
        return False

def wildCard(topCard):
    if (topCard == 0):
        t=0
        

#Card to Start off the game with while if nested loop to make sure its not a wild card eg: Skip
topCard = getCard()
notLegalCard = True
while (notLegalCard):
    if (topCard == "Change Color" or topCard == "Pick up 4" or topCard == "blue Skip" or topCard == "red Skip" or topCard == "green Skip" or topCard == "yellow Skip" or topCard == "red Reverse Direction" or topCard == "blue Reverse Direction" or topCard == "green Reverse Direction" or topCard == "yellow Reverse Direction" or topCard == "red Pick up 2" or topCard == "blue Pick up 2" or topCard == "green Pick up 2" or topCard == "yellow Pick up 2"):
        topCard = getCard()
    else:
        notLegalCard = False

#for loop to get 6 cards for user and store it in userCards dict
userCards = {}
for i in range(0, 6):
    card = getCard()
    userCards[i] = card
#for loop to get 6 cards for computer and store it in compCards dict
compCards = {}
for i in range(0, 6):
    card = getCard()
    compCards[i] = card
    
#While loop to run while user still has cards
while (len(userCards) > 0 or len(compCards) > 0):
    
    #print the current top card
    print("\n\n\t*** The Current Card is : " + topCard + " ***\n")
    #print out user Cards and ask user to chose one to play
    print("\nUser Cards : ")
    for i in userCards:  
        print("Card " + str(i) + " : " + userCards[i])
    userCardNum = input("\nPlease enter the number of the card you'd like to play,\n\nif you need to pick up a card just enter a 'y' : \n")
    
    #pick up a card if you cant play else select card
    if (userCardNum == "y" or userCardNum == "Y"):
        card = getCard()
        cardNum =(len(userCards))
        userCards[cardNum] = card
        
    else:
        #set values and run while loop to check if card is legal to play
        userCardNum = int(userCardNum)
        userCard = (userCards.pop(userCardNum))
        legalCard = False
        while (legalCard == False):
            legal = isLegal(topCard, userCard)
            if legal:
                legalCard = True
                topCard = userCard
            else:
                print("Invalid Card, please pick another.")
                break
        #if its true and its a wild card change color of theme
        if legalCard:
            cardDict = {1: 'Blue', 2: 'Green', 3: 'Red', 4: 'Yellow'}
            if (userCard == "Change Color"):
                colorNum = int(input("Please Enter the number of the desired color you want : \n1 : Blue\n2 : Green\n3 : Red\n4 : Yellow\n"))
                color = (cardDict[colorNum] + " is the new color theme.")
                topCard = color
            elif (userCard == "Pick up 4"):
                colorNum = int(input("Please Enter the number of the desired color you want : \n1 : Blue\n2 : Green\n3 : Red\n4 : Yellow\n"))
                color = (cardDict[colorNum] + " is the new color theme.")
                topCard = color





if (len(userCards) > 0):
    print("\n\n\t***  Congradulations! ***\n\n\tYou beat the Computer")
else:
    print("\n\n\tSorry! You Lost.")
