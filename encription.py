#This is a simple app that allows you to encript or decript a sentence the user gives
#The encription key is something random i made so theres no spesific order to it
#
#Made by : Robert Zeelie
#
#ask the user if they would like to encript or decript a sentence
choice = int(input("Welcom to RAZ Tech Enription\n\n\t0 : Exit\n\t1 : Encript\n\t2 : decript\n\nPlease Select a number :  "))

#while loop to continue until user specifies break
while(choice != 0):
    #elif statments to figure out if the user wants to encript or decript
    
    if(choice == 1):
        
        #dictionare to encript sentence
        encriptKey = {'a':'2','b':'289', 'c':'57', 'd':'95', 'e':'39', 'f':'87', 'g':'47', 'h':'12', 'i':'23', 'j':'51', 'k':'874', 'l':'1', 'm':'33', 'n':'191', 'o':'731','p':'219', 'q':'552', 'r':'338', 's':'76', 't':'484', 'u':'611', 'v':'929', 'w':'451', 'x':'6', 'y':'19', 'z':'345', ' ':'0'}        
        
        encriptString = input("\nYou Selected To Encript A Sentence\n\nPlease Enter A Sentence Below :\n")
        encriptedString = ""
        
        #for loop to convert each character of the users input to the encripted format
        for char in encriptString:
            encriptedString += (encriptKey[char] + ',')
        encriptedString = encriptedString[:-1]
        #open a file and write the encripted sentence to it
        textFile = open("EncyrptedInfo.txt","w")
        textFile.write("Encripted Sentence : " + encriptedString)
        textFile.close()
        
        #ask the user if they would like to do more or exit
        choice = int(input("\n\t0 : Exit\n\t1 : Encript\n\t2 : decript\n\nPlease Select a number :  "))

    elif(choice == 2):
        
        #dictionare to decript sentence
        decriptKey = {2:'a', 289:'b', 57:'c', 95:'d', 39:'e', 87:'f', 47:'g', 12:'h', 23:'i', 51:'j', 874:'k', 1:'l', 33:'m', 191:'n', 731:'o', 219:'p', 552:'q', 338:'r', 76:'s', 484:'t', 611:'u', 929:'v', 451:'w', 6:'x', 19:'y', 345:'z', 0 :' '}
        #get user input as a string
        decriptString = input("\nYou Selected To Encript A Sentence\n\nPlease Enter A Sentence Below :\n")
        decriptArr = decriptString.split(',')#split on commas
        decriptedString = ""
        
        #for loop to convert each character of the users input to the decripted format
        for item in decriptArr:
            num = int(item)#cast to int
            #if num in key then add
            if num in decriptKey:
                decriptedString += decriptKey[num]
            else:
                print(str(num) + " is not a valid character")
                decriptedString += "_"
        #open a file and write the decripted sentence to it
        textFile = open("DecyrptedInfo.txt","w")
        textFile.write("Decripted Message : " + decriptedString) 
        textFile.close()
        choice = int(input("\n\t0 : Exit\n\t1 : Encript\n\t2 : decript\n\nPlease Select a number :  "))
    
    #if user input is out of bounds
    elif(choice > 2 or choice < 0):
        print("\n\n* The Number you entered is  not valid *\n\n")
        choice = int(input("\n\t0 : Exit\n\t1 : Encript\n\t2 : decript\n\nPlease Select a number :  "))
 
#Exiting statement   
print("\n\n\tYou Are Exiting\n\n\tGoodbye\n")