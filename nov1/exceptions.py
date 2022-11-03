#author yaz c

from re import T


number = -1
while True:                     #makes it loop 
    try:    
        number = int(input("Enter a Whole Number: "))
        break
    except ValueError:
        print("Sorry, not a valid number")

print(f"Your number is {number}")