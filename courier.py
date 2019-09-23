cost = 0
insurance = 0
giftPrice = 0
speed = 0
totalCost = 0
delivery = 0

name = input(" Welcome to our Courier, please enter your name? : ")

price = float( input(" What is the price of the package " + name + "? : "))
# puts it into 2 decimal places
price = "%.2f" % price


dist = float( input(" What is the total distance the package would have to travel in Km's before reaching you? : '"))


trav = input(" Would you like the package to travel by air (R0.36 per km)\n or by road (R0.25 per km)? \n(Please answer with  either 'air' or with 'road') : ")
trav = (trav.lower())
if trav == "air" :
   cost += float(0.36)
elif trav == "road" :
   cost += float(0.25)
else :
   print (" Option was not selected ")
   
   
insure = input(" Would you like to insure your package " + name + "? \n full insurance = R50.00 \n limited insurance = R25.00 \n (please answer with either 'full' or with 'limited') : ")
insure = (insure.lower())
if insure == "full" :
   insurance += float(50.00)
elif insure == "limited" :
   insurance += float(25.00)
else : 
   print (" option was not selected ")
   
   
gift = input(" Would you like to send a gift with your package " + name + "? \n gift = R15.00 \n (please answer with either 'yes' or with 'no') : ")
gift = (gift.lower())
if gift == "yes" :
   giftPrice += float(15.00)
   
   
prio = input(" How fast would you like your package to get here " + name + "?\n Priority = R100.00 \n Standard = R20.00\n (Please answer with either 'priority' or with 'standard') ")
prio = (prio.lower())
if prio == "priority" :
   speed += float(100.00)
elif prio == "standard" :
   speed += float(20.00)
else :
   print(" Option not selected ")
   
   
delivery = (float(dist * cost))
   




totalCost = (float(speed) + float(giftPrice) + float(insurance) + float(delivery) + float(price))
totalCost = "%.2f" % totalCost
print(" The total price for the package amounts to R"+(str(totalCost)) + "\n thank you " + name + " for using us, please proceed to payment options.")
   