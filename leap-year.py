year=input("please enter your year data:")
year=int(year)
if year % 400 ==0:
 print ("yes")
elif year % 100 ==0:
 print ("no")
elif year % 4 ==0:
 print ("yes")
else:
 print ("no")
