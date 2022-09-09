#author-yazmin cooper
import math

print("Grades")
hw = float(input("Homework Grade: "))
ass = float(input("Assignments: "))
mid = float(input("Midterm: "))
fnl = float(input("Final: "))
fg = hw*.2 + ass*.3 + mid*.2 + fnl*.3

print(f"You earned a {round(fg,1)}% ")

if fg >= 89.5:
    print("A")
elif fg >= 79.5:
    print("B")
elif fg >= 69.5:
    print("C")
elif fg >= 59.5:
    print("D")
elif fg <=59:
    print("F")
else:
    print("You failed :(")

print ("Goodbye!")

