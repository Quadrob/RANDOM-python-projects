
# this function takes in the amount of nights and room cost and calculats the amount to stay there
def hotelCost(amountNights, roomCost):
   totalCostH = (amountNights * roomCost)
   return totalCostH
   
#this funtion takes the users desired city destination and finds the cost of travl
def planeCost(city):
   city.lower()
   if city == "durban":
      flightCost = 1500
   elif city == "cape town":
      flightCost = 2000
   elif city == "johannesburg":
      flightCost = 1000
   elif city == "port elizabeth":
      flightCost = 1500
   elif city == "mossel bay":
      flightCost = 1000
   return flightCost
   
# this function takes the amount of days the user would like to rent a car for
def carRental(amountDays):
   totalCostC = (amountDays * 100)
   return totalCostC
   
#this function takes all the calculated amounts from the above functions and adds them to find the total cost of the holiday
def holidayCost(city,amountDays,amountNights,roomCost):
   holidayCost = (hotelCost(amountNights, roomCost)+planeCost(city)+carRental(amountDays))
   return("A holiday to " + city + " will cost you : R" + str(holidayCost))


userInput = input("Would you like to go on holiday ?\nYes or No : ")
userInput.lower()

# this if statement checks the users input and if true will continue to ask the user for more information for it to perform calculations
if userInput == "yes" :

   city = input("Please enter a City you would like to travel to :\nDurban\nCape Town\nJohannesburg\nPort Elizabeth\nMossel Bay : ")
   
   carOption = input("would you like to rent a car ?: ")
   carOption.lower()
   if carOption == "yes" :
      amountDays = int(input("Please enter how many days you would like to rent the car for : "))
      
   #this gets the user to chose a desired room option to find the value of the room cost to pass on to the funtion
   roomOption = input("There are 3 room choices :\nGold = R1000 a night\nSilver = R750 a night\nBronze = R500 a night\nPlease enter either 'Gold', 'Silver' or 'Bronze' : ")
   roomOption.lower()
   if roomOption == "gold" :
      roomCost = 1000
   elif roomOption == "silver" :
      roomCost = 750
   elif roomOption == "bronze" :
      roomCost = 500
   else :
     print("No valid room option was choosen")
     
   amountNights = int(input("Please enter the amount of nights you would like to stay : "))
     
   print( holidayCost(city,amountDays,amountNights,roomCost))