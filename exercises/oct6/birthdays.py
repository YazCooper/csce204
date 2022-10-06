#author-yaz c

from datetime import date

birthdays = [date(2022,12,4), date(2023,5,14), date(2023,8,19), date(2023,5,22,), date(2023,10,31)]


#loop through and display birthdays

for bday in birthdays:
    num_days = (bday - date.today())
    print (bday.strftime("%b %d"), end ="")
    print(f"- is in {num_days} days")

















