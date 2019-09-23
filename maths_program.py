#first i define my variables and a list which will be used to store thr results before writing them to the new file
outputList = []
fileContent = ""
average = 0
i = 4
j = 0
n = 0

file = open("input.txt","r" )

for line in file :
   #the for loop reads the info from the file and then turns it to lower case for comparison 
   fileContent = line 
   fileContent = (fileContent.lower())
 
#this first if statment checks to see if the file requires the integer minimum,if so it finds the min and adds it to our outputlist
   if fileContent[3:6] == "min" :
      outputList.append(("The min of [" + fileContent[7:-1] + "] is " + fileContent[7] + ". "))
      
#this checks for maximum, if so finds the max and adds it to the output list
   if fileContent[0:3] == "max" :
      outputList.append(("The max of [" + fileContent[4:-1] + "] is " + fileContent[-2] + ". "))
      
#this checks for average, it so it enters a for loop for the duration of the file content
   if fileContent[0:3] == "avg" :

#i begins at 4 because the begining of our fileContent is letters which is not used to find the average
      for i in range(4,len(fileContent)):

#this if statment makes sure only integers enters our average variable and once all the numbers have been recorded the average is calculatedand then given to our output list
         if fileContent[i] != "," :
            average = average + float(fileContent[i])
            j += 1
            
      average = float(average)
      average = (average/j)
      outputList.append(("The avg of [" + fileContent[4:] + "] is " + str(average) + ". "))
   
file.close()

file = open("output.txt","w" )

for n in range(0,len(outputList)):
   info = (str(outputList[n]))
   file.write((info + "\n"))
   
file.close()
