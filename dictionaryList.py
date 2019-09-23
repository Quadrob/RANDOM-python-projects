abbreviations = {"BA":"Bachelor of Arts",
"BS":"Bachelor of Science",
"MA":"Master of Arts",
"JD":"Juris Doctor",
"DC":"Doctor of Chiropractic"
}

abbreviations["PA"] = "Personal Assistant"
abbreviations["MD"] = "Managing Director"
abbreviations["VP"] = "Vice President"

userAbbreviation = input("Please enter an abbreviation : ")
userAbbreviation = (userAbbreviation.upper())

if userAbbreviation in abbreviations :
   print(userAbbreviation + " means " + abbreviations[userAbbreviation])
   
else:
   print("Unknown Abbreviation")