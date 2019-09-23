numberSort = []

file = open("numbers1.txt","r" )

#a loop used to store the info captured from the txt file as an integer in the empty list
for line in file :
   numberSort.append(int(line))

file.close()

file = open("numbers2.txt","r" )

for line in file :
   numberSort.append(int(line))
   
file.close()

#sorts the integers in order of smallest to largest
numberSort.sort()

#create a new file where the results will be writen to and stored
file = open("allNumbers.txt","w")

for i in range(0,len(numberSort)) :
    number = str(numberSort[i])
    file.write(number + "\n" )

file.close()
