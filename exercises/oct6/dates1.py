#author-yaz c

from datetime import date, time, datetime      #to use dates

todays_date = date.today()
#print (todays_date)
print(todays_date.strftime("%B:%d -%A,%Y  "))   #format date into a string

halloween = date(2022,10,31)
print(f"Halloween:", end = "")  #end=" means dont go to a new line"
print(halloween.strftime("%m/%d/%Y"))

class_time = time(11,40)
print("Class Time is ", end ="")
print(class_time.strftime("%I:%M%p"))

pie_day = datetime(2023,3,14,13,59)
print("Pie Day is ", end="")
print (pie_day.strftime("%m/%d %I.%M"))

birthdaytext = input("Enter Birthday (MM/DD/YYYY): ").strip()
#Convert text into a date
birthday = datetime.strptime(birthdaytext,"%m/%d/%Y")  #take text and format the date this way when displaying

print("My Birthday is ",end="")
print(birthday.strftime("%b %d"))

#how long until pi day

#dates are diff from times and date times. cant subtract dates from datetimes
days = (pie_day-datetime.now()).days   #.days will tell how many days until
print(f"You have {days} days til pie day. ")















