import random

minNum = 1
maxNum = 6

roll_again = "yes"

while roll_again == "yes" or roll_again == "y":
    print ("Rolling the dices....\n")
    print ("The values are :")
    print ("Die 1 : " + str(random.randint(minNum, maxNum)))
    print ("Die 2 : " + str(random.randint(minNum, maxNum)))

    roll_again = input("\nWould you like to Roll the dices again?\n\tYes or No :\n")