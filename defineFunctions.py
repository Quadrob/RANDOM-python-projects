#Requirment 1

# defining my function which checks the users input, if yes it prints out the list (weekDayList)
def weekDays(userInput) :
   if userInput == "yes" :
      print(weekDayList)
      
#a list containting all the weekdays
weekDayList= ["Monday","Tuseday","Wednesday","Thursday","Friday","Saturday","Sunday"]

userInput = input("Please enter 'yes' to display the weekdays : ")

weekDays(userInput)


#Requirment 2

#defining my function which acceptes the users string and splits it using white space forming a list
def wordReplace(userInput) :
   words = (userInput.split())
   #this loop checks for even numbers and if so changes that particular word from the user to hello so that the final will display every second word as hello
   for i in range(0,(len(words))):
      if i % 2 == 0 : 
         words[i] = "Hello"
   print(words)
   
     
userInput = input("Please enter a sentence : ")

wordReplace(userInput)