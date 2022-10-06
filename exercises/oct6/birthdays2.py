#author - yaz c

from datetime import date
birthdays = {
    "Kwame": date(2023,4,20),
    "Daquan": date(2023,8,17),
    "Joel": date(2023,9,8),
    "Diana": date(2023,7,4),
    "Alecia": date(2023,3,14)

}


#loop through and display friends and birthdays

for friend in birthdays:
    print(f"{friend} - ")
    print(birthdays[friend].strftime("%m/%d"),end="")   #access birthday for the friend
    numdays = (date.today() - birthdays[friend]).days
    print(f"- {numdays} days ")

    

