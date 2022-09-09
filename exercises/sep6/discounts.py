#author-yazmin cooper





day = input("Enter day of week: ").lower().strip()   #lower=convert input to lowercase   #strip=take off leading and tailing white space

if day == "monday" or day == "mon" :          #<---must be lowercase to work (ex. monday 
    print ("Moes Monday")
elif day ==  "tuesday" or day == "tues":
    print ("Taco Tuesday")
elif day == "wednesday" or day == "wed":
    print ("Wine Wednesday")
elif day == "thursday" or day == "thur":
    print ("Truffle Thursday")
elif day ==  "friday" or day == "fri":
    print ("Fry Friday")
else:
    print ("No Discount")