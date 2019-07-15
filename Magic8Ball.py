import random

def magic_8ball():
    
    x = input("\t** Magic 8 Ball **\n\n\tPress Enter to Exit\n\t-------------------\n\nWhat is your question? \n")
    Eightball_list = ["It is certain", "it is decidedly so", "Yes", "YES", "without a doubt", "definit", "no", "NO", "Looks good", "Outlook good","You may rely on it","Ask again later","Concentrate and ask again","Reply hazy, try again","My reply is no","My sources say no"]
    
    if x == "" :
        print ("Exiting...")
    else:
        print (" ")
        print (random.choice(Eightball_list))

magic_8ball()