outputList = []
fileContent = ""
average = 0
percent = 0
add = 0
i = 4
n = 0

file = open("input_optional.txt","r" )

for line in file :
   fileContent = line 
   fileContent = (fileContent.lower())
   j = 0
   p = 0
   
   if fileContent[0:3] == "min" :
      outputList.append(("The min of [" + fileContent[4:-1] + "] is " + fileContent[4] + ". "))
      
   if fileContent[0:3] == "max" :
      outputList.append(("The max of [" + fileContent[4:-1] + "] is " + fileContent[-2] + ". "))
   
   if fileContent[0:3] == "avg" :
      for i in range(4,(len(fileContent)-1)):
         if fileContent[i] != "," :
            average = average + float(fileContent[i])
            j += 1
      average = float(average)
      average = (average/j)
      outputList.append(("The avg of [" + fileContent[4:-1] + "] is " + str(average) + ". "))
         
#this is the same loop i use for both percentiles, please tell me where im making the mistake?
   if fileContent[0:3] == "p90" :
      for i in range(4,(len(fileContent))):
         if fileContent[i] != "," :
            j += 1
      p = (90\100)
      answer = (int(j*p))
      answer = int( answer + 4)
      outputList.append(("The " + fileContent[1:3] + "th percentile of [" + fileContent[4:-1] + "] is " + str(fileContent[answer]) + ". "))
      
      if fileContent[0:3] == "p70" :
      for i in range(4,(len(fileContent))):
         if fileContent[i] != "," :
            j += 1
      p = (70\100)
      answer = (int(j*p)
      answer = int( answer + 4)
      outputList.append(("The " + fileContent[1:3] + "th percentile of [" + fileContent[4:-1] + "] is " + str(fileContent[answer]) + ". "))

   if fileContent[0:3] == "sum" :
      for i in range(4,(len(fileContent)-1)):
         if fileContent[i] != "," :
            add = add + int(fileContent[i])
      outputList.append(("The sum of [" + fileContent[4:-1] + "] is " + str(add) + ". "))

file.close()

file = open("output.txt","w" )

for n in range(0,len(outputList)):
   info = (str(outputList[n]))
   file.write((info + "\n"))
   
file.close()
