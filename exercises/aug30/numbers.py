#Author:Yazmin Cooper

import math
#incrementing age
#age = int(input("Enter Age: ")) #float=ability to insert decimal numbers
#first_name = input("Enter First Name: ")
#last_name = input("Enter Last Name: ")
#future_age = age + 10
#print(f"{first_name} {last_name}, next decade you will be {future_age}!")

#Pizza Party
#guests = int(input("Enter Number of Guests: "))
#slices = float(input("Enter Average slices per Guest: "))
#total_pizzas = math.ceil(guests * slices /8)
#print(f"You should order {total_pizzas} pizzas.")

# one (/) is decimal | but | (//) is whole numbers

#Chicken and Eggs

#eggs = int(input("How many eggs: ")) #28
#carton = eggs//12
#left_over = eggs % 12 # (%) is called modulus and gives the remainder from an equation (eggs - carton *12)
#print(f"""You need {carton} cartons. 
#You have {left_over} eggs left over.""")

#Paid
#per_hour = float(input("How much do you get paid per hour: "))
#overtime =  (per_hour * 1.50)
#print(f"You should make $ {round(overtime,2)} per hour.")

#Grades
print("Lets Calculate Your Class Grade")
assignments = float(input("Assigments: "))
exercises = float(input("Exercises: "))
midterm = float(input("Midterm: "))
final = float(input("Final: "))
final_grade = assignments *.55 + exercises*.15+midterm*.15+final*.15
print(f"Your final grade is {round(final_grade,1)}.")