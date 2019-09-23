#simple ATM project for mock interview
#
#   Robert Zeelie   created 17/09/19
#
#To login: Account Number : |  0101  |    or     |  0202  |
#                           |        |           |        |
#                Password : |  1000  |    or     |  2000  |

import random

#function to print out airtime
def airtime(amount):
    #generates a rrandom 10 digit code
    randomCode = random.randint(1000000000,10000000000)
    #check what amount and print the airtime and its code
    if (amount == 1):
        print("\n\n\t\t** $1 Airtime **\nCall #103 and follow instructions and find required code below:\n\t\tCode: " + str(randomCode) + "\n\n")
    elif (amount == 2):
        print("\n\n\t\t** $10 Airtime **\nCall #103 and follow instructions and find required code below:\n\t\tCode: " + str(randomCode) + "\n\n")
    elif (amount == 3):
        print("\n\n\t\t** $20 Airtime **\nCall #103 and follow instructions and find required code below:\n\t\tCode: " + str(randomCode) + "\n\n")
    
#a function to buy something with account
def buySomething(accountNum, accountAmount):
    #gets what the user wants
    item = int(input("\n\nList of items to purchase :\nAirtime : 1\nFood : 2\n\nExit : 0\n\nPlease enter the number of the item youd like to purchase : "))
    #if 0 exit else checks what user wants
    if (item == 0):
        showBalance(accountNum, accountAmount)
    #if 1 displays different amounts of airtime for user to choose
    elif (item == 1): 
        #gets the amount of airtime
        amount = int(input("\n\nPlease choose your amount:\n$1 : 1\n$10 : 2\n$20 : 3\n\nExit : 0\n\nPlease enter a number : "))
        if (amount == 0):
            showBalance(accountNum, accountAmount)
        elif (amount == 1):
            #checks if possible
            if (1 < accountAmount[accountNum]):
                newAmount = (accountAmount[accountNum] - 1)
                accountAmount[accountNum] = newAmount
                print("\nYour new amount is : " + str(accountAmount[accountNum]))
                airtime(amount)
                showBalance(accountNum, accountAmount)
        elif (amount == 2):
            if (10 < accountAmount[accountNum]):
                newAmount = (accountAmount[accountNum] - 10)
                accountAmount[accountNum] = newAmount
                print("\nYour new amount is : " + str(accountAmount[accountNum]))
                airtime(amount)
                showBalance(accountNum, accountAmount)
        elif (amount == 3):
            if (20 < accountAmount[accountNum]):
                newAmount = (accountAmount[accountNum] - 20)
                accountAmount[accountNum] = newAmount
                print("\nYour new amount is : " + str(accountAmount[accountNum]))
                airtime(amount)
                showBalance(accountNum, accountAmount)
    #if 2 displays the different food for user to choose
    elif (item == 2):
        #gets the food type
        amount = int(input("\n\nPlease choose your Food:\n$2 Spicey Chips : 1\n$1 Bar One : 2\n$2 Water : 3\n\nExit : 0\n\nPlease enter a number : "))
        if (amount == 0):
            showBalance(accountNum, accountAmount)
        #checks if possible
        elif (amount == 1):
            if (2 < accountAmount[accountNum]):
                newAmount = (accountAmount[accountNum] - 2)
                accountAmount[accountNum] = newAmount
                print("\nYour new amount is : " + str(accountAmount[accountNum]))
                print("\n\n\t\t** Here's Your: Spicey Chips **\n\n")
                showBalance(accountNum, accountAmount)
        elif (amount == 2):
            if (1 < accountAmount[accountNum]):
                newAmount = (accountAmount[accountNum] - 1)
                accountAmount[accountNum] = newAmount
                print("\nYour new amount is : " + str(accountAmount[accountNum]))
                print("\n\n\t\t** Here's Your: Bar One **\n\n")
                showBalance(accountNum, accountAmount)
        elif (amount == 3):
            if (2 < accountAmount[accountNum]):
                newAmount = (accountAmount[accountNum] - 2)
                accountAmount[accountNum] = newAmount
                print("\nYour new amount is : " + str(accountAmount[accountNum]))
                print("\n\n\t\t** Here's Your: Water **\n\n")
                showBalance(accountNum, accountAmount)
            
#a function to withdraw from account
def withDraw(accountNum, accountAmount):
    #gets amount
    amount = int(input("\n\n\tMake a Withdrawl\n\nIf you do not want to withdraw anything please enter : 0\n\nPlease enter an ammout you would like to withdraw :"))
    #checks if possible
    if (amount > 0):
        if (amount < accountAmount[accountNum]):
            newAmount = (accountAmount[accountNum] - amount)
            accountAmount[accountNum] = newAmount
            print("\nYour new amount is : " + str(accountAmount[accountNum]))
            showBalance(accountNum, accountAmount)
        else:
            showBalance(accountNum, accountAmount)
            
#a function to deposite to account
def deposit(accountNum, accountAmount):
    #gets amount
    amount = int(input("\n\n\tMake a Deposite\n\nIf you do not want to deposit anything please enter : 0\n\nPlease enter an ammout you would like to deposit :"))
    #check if possible or if it must exit
    if (amount > 0):
        originalAmount = accountAmount[accountNum]
        newAmount = amount + originalAmount
        accountAmount[accountNum] = newAmount
        print("\n\tYour new amount is : $" + str(accountAmount[accountNum]))
        showBalance(accountNum, accountAmount)
    else:
        showBalance(accountNum, accountAmount)
        
#a function to show balance and gives the user options on what to ddo
def showBalance(accountNum, accountAmount):
    #prints account balance and asks user what they want to do
    print("\nThe Balance for account " + accountNum + " is : $" + str(accountAmount[accountNum]))
    action = int(input("\n\tTo make a deposit enter : 1\n\tTo make a withdrawl enter : 2\n\tTo buy items enter : 3\n\n\tTo exit enter : 0\n\nEnter your choice : "))
    #to figure out what the user would like to do and then calls function
    if(action == 0):
        print("\n\nYou Are being Logged Out\n\n\tgoodbye\n")
    elif(action == 1):
        deposit(accountNum, accountAmount)
    elif(action == 2):
        withDraw(accountNum, accountAmount)
    elif(action == 3): 
        buySomething(accountNum, accountAmount)
        
#a login function
def login(accountNum, password):
    #2 dictionaries wich contains account password and balance of accounts
    accounts = {'0101' : 1000, '0202' : 2000}
    accountAmount = {'0101' : 200, '0202' : 400}
    #to make sure user information is valid
    if (accountNum in accounts):
        if (accounts[accountNum] == password):
            print("\n\tWelcome\n")
            showBalance(accountNum, accountAmount)
        else:
            print("\n\tincorrect password")
    else:
        print("\n\tAccount does not exist")

#make sure it is run as main
if __name__ == "__main__":
    #takes the account number and password and calls login function with them with them
    accountNum = input("Please enter account number : ")
    password = int(input("\nPlease enter your 4 digit pin : "))
    login(accountNum, password)