import random



name = input(" Welcome to the lotto!\n Please enter your name to begin : ")

lottoNum1 = random.randint(1,9)
lottoNum1 = int(lottoNum1)

lottoNum2 = random.randint(1,9)
lottoNum2 = int(lottoNum2)



userNum1 = int( input(" Please enter a number from 1 to 9 to play and stand a chance to win! : "))

userNum2 = int( input(" Please enter a number from 1 to 9 to play and stand a chance to win! : "))



print (" The lotto numbers are : " + str(lottoNum1) + str(lottoNum2) + " \n Your numbers were : " + str(userNum1) + str(userNum2))


if userNum1 == lottoNum1 and userNum2 == lottoNum2 :
   print (" Congradulations you have an exact match, you win /nR10.000.00! ")
   
elif userNum1 == lottoNum2 and userNum2 == lottoNum1 :
   print (" Congradulations you have all the digits, you win /nR5.000.00!")
   
elif userNum1 == lottoNum1 or userNum2 == lottoNum2 :
   print (" Congradulations you have one correct digit, you win /nR1.000.00! ")

elif userNum1 == lottoNum2 or userNum2 == lottoNum1 :
   print (" Congradulations you have one correct digit, you win /nR1.000.00! ") 
   
else : 
   print (" Sorry no match ")