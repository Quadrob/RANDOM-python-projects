
#collecting the information from file
fileContent = ""

file = open("input.txt","r" )

for line in file :
   fileContent = fileContent + line
   
file.close()

#count the amount of characters in the txt file
characters = len( fileContent ) 

#count the amount of words in the txt file
words = len( fileContent.split())

#count the amount of lines in the txt file
lines = len( fileContent.splitlines())

print(" Characters = " + str(characters) + "\n Words = " + str(words) + "\n Lines = " + str(lines))

#list defining letters in this case vowels
vowels = [ "a","e","i","o","u" ]

#defining the variables
num = 0
amountOfCharacters = 0

#defining an empty list to be used later on
frequency = []

#format the txt file tolower case for comparison to the vowles
fileContent = (fileContent.lower())

#loop to run while there are still letters in the list vowels
for letter in vowels :
   
   #counts the amount of times the particular vowel at that point in the loop     
   # is used
   amountOfCharacters = fileContent.count(letter)
   
   #adds both the vowel and amount of times it was 
   # used to the list (frequency)
   frequency.append((letter + " : " + str(amountOfCharacters)))
   
print (" The amount of times each vowel is used : ")
print ( frequency ) 
