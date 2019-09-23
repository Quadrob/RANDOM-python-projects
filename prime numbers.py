


userNum = int(input(" Enter a random number larger than 1 \n\n (1<) \n\n and we will tell you if its a prime number : "))

#test to see if its greater than 1

while userNum <= 1 :
   userNum = int(input(" Please enter a random number larger than 1 \n (1<) \n and we will tell you if its a prime number : "))
 # test to see if its prime
 # first set the range from 2 to the entered number as to let the computer know when to stop
   
for i in range(2,userNum) :

#now we divid it but all the numbers between 2 and itselfe, if theres no remainder its not prime

   if userNum % i == 0 : 
      print( str(userNum) + " is not a prime number! "); break ;
      
   else :
      print( str(userNum) + " is a prime number! "); break ;