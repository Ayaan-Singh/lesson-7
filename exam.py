attendence = int(input("enter your attendence"))
medicalcause = (input("do you have a medical cause (please enter Y OR N)"))
medicalcause = medicalcause.upper()
if (medicalcause == "Y"):
    print("you are allowed to enter")
elif (attendence > 75):
    print("you are allowed to enter")
else: 
    print ("you are not allowed to enter")