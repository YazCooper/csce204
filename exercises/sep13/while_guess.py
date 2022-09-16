#author - yaz c.
import random

goal = random.randint(1,100)

print(f"The goal is {goal}")


print("Welcome to our guessing game!")

while True:
    num = int(input("Enter a number between 1 and 100: "))
    if num == goal:
        print("Correct!")
        break
    elif num > goal:
        print("Sorry! That was too high")
    elif num < goal:
        print("Sorry! That was too low")
    again = input("Do you want to guess again? (Y)es or (N)o: ").strip().lower()
    if again == "n" or again == "no":
        break




print("Goodbye!")
        

