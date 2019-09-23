temp = False
weekend = False
sunny = False

name = input(" Welcome to cloths selecter, please enter your name?: ")

tempChe = input(" hello " + name + ", Now to begin your outfit, what is the temperature in degrees celsius?: ")
tempChe = int(tempChe)
if tempChe > 20 :
   temp = True
   print (" You should wear a short sleeve shirt so you dont get hot.")
else : 
   print (" You should wear a long sleeve shirt so you dont get sick.")
   
weekChe = input(" Plase answer the questions with either a 'yes' or a 'no'. Right " + name + ", is it the weekend?:")
weekChe = (weekChe.lower())
if weekChe == "yes" :
   weekend = True
   print (" and you should wear shorts because its the weekend. ")
else :
   print (" Time to work " + name + ", you should wear jeans. ")
   
sunChe = input(" Please answer the questions with either a 'yes' or a 'no'. is it sunny outside?: ")
sunChe = (sunChe.lower())
if sunChe == "yes" :
   sunny = True
   print (" Don't want to get sunburnt, you should wear a cap!: '")
else :
   print (" Don't want to get wet, you should wear a raincoat!: '")
   
print (" Enjoy your day! ")
   







