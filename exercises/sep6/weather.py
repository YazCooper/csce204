from genericpath import commonprefix


#author-yazmin cooper 

print("What to wear")

temp = float(input("Enter Temp: "))
pcp = input("Enter precipitation (r), (s), or (n): ").strip().lower()

if temp <= 32 and pcp == "s":
    print("You should wear a snowsuit")
elif temp <= 70 and pcp == "r":
    print("You should wear a rain jacket.")
elif temp >= 80 and pcp == "r":
    print("You can wear a swimsuit")
else:
    print("You choose")