#collecting the information from file
fileContent = ""

file = open("DOB.txt","r" )

for line in file :
   fileContent = fileContent + line
   
file.close()

numOfLines = len(fileContent.splitlines())

#declare the variables
i = 0
n1 = 0
n2 = 2

#loop to separate the names and birth dates and print them 1 under the other
for i in range(0,(numOfLines)) :
   i = i + 1
   print(str(i) + ". " + (" ".join(fileContent.split()[n1:(n1+2)])))
   print(str(i) + ". " + str((" ".join(fileContent.split()[n2:(n2+3)]))))
   n1 += 5
   n2 += 5
