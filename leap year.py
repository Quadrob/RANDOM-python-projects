



userYear = int( input(" welcome to leap year calculator\n Please enter a year\n example '1997' : "))


startYear = userYear


userNum = int( input(" please enter the amount of years you would like us to check : "))


for i in range(0,userNum) :
   if startYear%4 == 0 :
      print(str(startYear) + " is a leap year ! ")
      
   else :
      print(str(startYear) + " is not a leap year ! ")
   
   
   startYear += 1
   
   
print(" the end ")