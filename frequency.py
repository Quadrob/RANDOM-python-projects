#defining my variables
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
i = 0
letter = ""
numberOf = 0
frequency = []

#input from user and formats it first to lower case then takes away any spaces
sentence = input(" Please enter a string : ")
sentence = sentence.lower()
sentence = sentence.strip(" ")

#a loop for all the letters in the alphabet
for i in range (0,(len(alphabet))) :

    #stores the number fot times a letter is used
    numberOf = sentence.count(alphabet[i])

    #stores the letter at that particular time of the loop for refernce
    letter = alphabet[i]
       
    #stores the letter and number in a list to later be printed out
    frequency.append((str(letter) + " : " + str(numberOf)))
    
print(frequency)
       
       
    
