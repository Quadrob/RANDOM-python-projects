# declairing variables
haveLenght = False
upCase = False
lowCase = False
haveNum = False
truAnswers = 0
suitPass = False

# start
name = input(" Welcome to password strenght test! Please tell us your name?: ")

# if statement to check lenght
lenCheck = input(" Hello " + name + ", please answer with a 'yes' or a 'no', is your password 6 or more characters long?: ")
lenCheck = ( lenCheck.lower())
if lenCheck == "yes" :
   haveLenght = True
   truAnswers += 1
   
#if statement to check uppercase
upCheck = input(" Does your password contain Uppercase letters?: ")
upCheck = (upCheck.lower())
if upCheck == "yes" :
   upCase = True
   truAnswers += 1
   
#if statement to check lowercase
lowCheck = input(" Does your password contain Lowercase letters?: ")
lowCheck = (lowCheck.lower())
if lowCheck == "yes" :
   lowCase = True
   truAnswers += 1
   
#if statement to check number of correct answers, if there is less than 3 it will move on to the next question
if truAnswers == 3 :
   suitPass = True
   print (" Suitable Password ")
else:

   #if statement to check if there are numbers
   numCheck = input(" Does your password contain numbers?: ")
   numCheck = ( numCheck.lower())
   if numCheck == "yes" :
      haveNum = True
      truAnswers += 1
   
   # final check to see if there are 3 correct answers if not display fix password
   if truAnswers == 3 :
      suitPass = True
      print (" Suitable Password ")
   else :
      print (" Fix your Password ")
   
   