dnaResult = []
fileContent = ""
fileContent1 = ""
fileContent2 = ""
mutateFile = ""
normalFile = ""

#this function takes the users DNA sequence input and slpits it on every third character in the sequence (the code in line 2) and then runs a for loop for each set of 3 characters to test which Amino Acid the 3 characters form and adds the Acids accronym to the empty list which is returned at the end of the function
def translate(fileContent):
   sequence = [fileContent[i:i+3] for i in range(0, len(fileContent), 3)]
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

#i open the file and then read each line     
file = open("DNA.txt","r" )
fileContent = file.read()
file.close()

#then i make a for loop to go over each letter which was read from the file, if the latter is ‘a’ it mutates it ‘T’ and fix’s it ‘A’ and adds it to variables mutateFile and normalFile, if the letter is not ‘a’ it just adds the letter exactly as is to the same variables
for letter in fileContent:
   if letter == "a":
      mutateFile = (mutateFile + "T")
      normalFile = (normalFile + "A")
   else :
      mutateFile = (mutateFile + letter)
      normalFile = (normalFile + letter)

#next 2 functions open 2 new files and writes to each file one of the different variabls mutateFile and normalFile
file = open("mutatedDNA.txt","w")
file.write(mutateFile)
file.close()

file = open("normalDNA.txt","w")
file.write(normalFile)
file.close()

#the next 2 functions read from each file that was created above and runs them through the function “translate” to find the amino acids in each DNA sequence, i think this is where my error comes in, its when you call these to functions
file = open("mutatedDNA.txt","r")
fileContent1 = file.read()
print("These are the folowing Amino Acids found in the DNA sequence's found in the mutated DNA text file : '" + str(translate(fileContent1)))
file.close()

dnaResult.clear()

file = open("normalDNA.txt","r")
fileContent2 = file.read()
print("These are the folowing Amino Acids found in the DNA sequence's found in the normal DNA text file : '" + str(translate(fileContent2)))
file.close()

dnaResult.clear()
