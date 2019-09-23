namesList = []
name = ""
attempt = 0

number = int(input("please enter number of attempts : "))

while attempt != number :
   if attempt == number :
      break
   name = input("Please enter john to proceed : ")
   name.lower()
   if name == "john" :
      break
   else :
      namesList.append(name)
   attempt += 1
      
if attempt == number :
      print("Max Attempts reached!")
print ("Incorrect names: " + str(namesList))