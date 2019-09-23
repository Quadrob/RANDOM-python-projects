import random

def magic_8ball():
    
    x = input("\n\t** Magic 8 Ball **\n\n\tPress Enter to Exit\n\t-------------------\n\nWhat is your question? \n")
    Eightball_list = ["That is crazy!", "dont you dare", "Go for it", "definetly", "I would", "You wont know if you dont try", "its worth a shout", "why not", "oh yes", "sounds good", "looks good", "its promising", "just do it", "dont do it", "i wouldnt", "looks bleak", "you not getting younger", "sure thing", "give it a try", "dont knock it till you try it", "its for you", "its not for you", "follow your heart", "go get it", "you only live once", "what does your heart say", "listen to your heart", "listen to your head", "think about this first", "its yours for the taking", "yes", "visualize it", "grab it with both hands", "dont miss it", "dont let it slip through your hands", "i dont think so", "lets do this", "i advise against", "all against it", "all for it", "you have it in you", "take your time", "wait", "times not right", "not yet, YET", "slowly but surly", "just wait", "wait it out", "take your time", "it takes time", "are you ready?", "if you want it", "if you want it, get it", "think about this", "use your head", "have you thought this through", "are you ready", "proper yoursself", "get it", "times in your favour", "times not in your favour", "highly doubt it", "big no no", "nahhhhh", "never", "nope","It is certain", "it is decidedly so", "Yes", "YES", "without a doubt", "definit", "no", "NO", "Looks good", "Outlook good","You may rely on it","Ask again later","Concentrate and ask again","Reply hazy, try again","My reply is no","My sources say no"]
    
    if x == "" :
        print ("Exiting...")
    else:
        print (" ")
        print ("\n\t*** " + random.choice(Eightball_list) + " ***")

magic_8ball()