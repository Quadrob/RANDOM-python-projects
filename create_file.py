#creating and opening a new write to txt file
studentFile = open("RegForm.txt","w")

#defining variable
i = 0

#input
studentNum = int(input("Please enter the amount of sudents you would like to register at this exam venue : "))

#loop used to collect ID's in range of amount of students and then writes the it to the txt file
for i in range(0, (studentNum)) :
   studentID = int(input("Please enter each students ID number : "))
   studentFile.write( str(studentID) + "\n" )
   
#close file
studentFile.close()

print("see you when exams start")
