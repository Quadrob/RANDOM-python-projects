#function for the addition of 2 numbers
def addNum(num1,num2):
   addResult = (num1 + num2)
   return addResult
   
#function for the subtraction of 2 numbers
def subtrackNum(num1,num2):
   subResult = (num1 - num2)
   return subResult
   
#function for the multiplication of 2 numbers
def multiplyNum(num1,num2):
   multiResult = (num1 * num2)
   return multiResult
   
#function for the division of 2 numbers
def divideNum(num1,num2):
   divResult = (num1 / num2)
   return divResult

userInput = 0
#user inputs which function theyd like to use
userInput = int(input("Menu :\n1 = addition\n2 = sutraction\n3 = multiplication\n4 = division\nPlease enter a number : "))

# these if / elif statments check which function the user requires,collectes the numbers from the user and calls the function using the numbers provided by the user and prints out the results
if userInput == 1:
   num1 = int(input("Please enter a number : "))
   num2 = int(input("Please enter a number : "))
   print("The answer is " + str(addNum(num1,num2)))

elif userInput == 2:
   num1 = int(input("Please enter a number : "))
   num2 = int(input("Please enter a number : "))
   print("The answer is " + str(subtrackNum(num1,num2)))    
   
elif userInput == 3:
   num1 = int(input("Please enter a number : "))
   num2 = int(input("Please enter a number : "))
   print("The answer is " + str(multiplyNum(num1,num2)))    
   
elif userInput == 4:
   num1 = int(input("Please enter a number : "))
   num2 = int(input("Please enter a number : "))
   print("The answer is " + str(divideNum(num1,num2))) 
   
else:
   print("Unrecognized option.")
   
