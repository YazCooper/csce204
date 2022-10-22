#author yaz c


def fahr_to_celc(fahrenheit):
    celcius = (fahrenheit-32)  *5/9
    return celcius
# THE TWO FAHRENHEIT VARIABLEs IN LINE 1 AND LINE 6 HAVE NO RELATION.JUST TEMP VARIABLE THAT EXIST FOR THE LIFETIME OF THE FUNCTION
def celc_to_fahr(celcius):
    fahrenheit = celcius* 9/5 + 32
    return fahrenheit

def miles_to_km(miles):
    km = miles*1.60934
    return km

def km_to_miles(km):
    miles=km*.621371
    return miles

print("Conversion Program")


while True:
    conv = input(""" 
                    1. Fahrenheit to Celcius, 
                    2. Celcius to Fahrenheit, 
                    3. Miles to Kilometers, 
                    4. Kilometers to Miles
                    Enter Type of Conversion or (Q)uit: """)
    if conv == "q":
        break
    elif conv == "1":
        inpt = int(input("Enter Fahrenheit: "))
        celcius = fahr_to_celc(inpt)
        print(f"Celcius is {round(celcius,2)}C")
    elif conv == "2":
        inpt = int(input("Enter Celcius: "))
        fahrenheit = celc_to_fahr(inpt)
        print(f"Fahrenheit is {round(fahrenheit,2)}F")
    elif conv == "3":
        inpt = int(input("Enter Miles: "))












