dnaResult = []

#this function takes the users DNA sequence input and slpits it on every third character in the sequence (the code in line 2) and then runs a for loop for each set of 3 characters to test which Amino Acid the 3 characters form and adds the Acids accronym to the empty list which is returned at the end of the function
def translate(userInput):
   sequence = [userInput[i:i+3] for i in range(0, len(userInput), 3)]
   for item in sequence:
      if item == "ATT" or item == "ATC" or item == "ATA" : 
         dnaResult.append(" I ")
      elif item == "CTT" or item == "CTC" or item == "CTA" or item == "CTG" or item == "TTA" or item == "TTG" : 
         dnaResult.append(" L ")
      elif item == "GTT" or item == "GTC" or item == "GTA" or item == "GTG" :
         dnaResult.append(" V ")
      elif item == "TTT" or item == "TTC" : 
         dnaResult.append(" F ")
      elif item == "ATG" : 
         dnaResult.append(" M ")
      else:
         dnaResult.append(" X ")
   return dnaResult
   
userInput = input("Please enter the DNA sequence : ")
userInput = userInput.upper()
userInput = (userInput.replace(" ",""))

if userInput == "ATGGTGCATCTGACTCCTGTGGAG":
   print("This DNA sequence displays signs of Sickle Cell Disease")
   
print("These are the folowing Amino Acids found in the DAN sequence in the oder you entered : " + str(translate(userInput)))