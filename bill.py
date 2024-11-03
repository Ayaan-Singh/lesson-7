units = int(input("units consumed"))
if (units < 50):
    print ("the cost is", (2.60*units)+25)
elif (units > 50 and units <= 100):
    print ("the cost is", (3.25*units)+35)
elif (units > 100 and units <= 200):
  print ("the cost is", (5.26*units)+45)
else :
    print ("the cost is", (8.45*units)+75)