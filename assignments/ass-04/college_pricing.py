#author:yazmin cooper

import math

days = int(input("How many days are you budgedting for? "))
books = int(input("How many books do you need? "))


textbook = 64.99 *1.07 * books
dorm_room = 184.99 * 1.07 * math.ceil(days/7)
breakfast = 3.85 *1.07 * days 
lunch = 8.95 *1.07 * days 
dinner = 12.79 * days * 1.07
total_exp = textbook + dorm_room + breakfast + lunch + dinner


print(f" Total expenses: ${round(total_exp,2)}")
