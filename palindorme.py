
#input from user
word = input(" Please enter a word : ")

#format input to lower case
lowerCase = word.lower()

#revers the string
reverse = (lowerCase[::-1])

#if statment to test the word
if reverse == lowerCase :
   print(" The word " + word + " is a palindorme!")
   
else :
   print(" The word " + word + " is not a palindorme!")