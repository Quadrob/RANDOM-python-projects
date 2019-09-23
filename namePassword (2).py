namesList = []
name = ""

while name != "john" :
   name = input("Please enter john to proceed : ")
   name.lower()
   if name == "john" :
      break
   else :
      namesList.append(name)
      
print ("Incorrect names: " + str(namesList))