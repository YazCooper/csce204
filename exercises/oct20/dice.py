#author-yaz c
import random

def roll():
    randroll = random.randint(1,6)
    randrolls_2 = random.randint(1,6)
    print(f"You rolled a {randroll} and a {randrolls_2}")
    
    return randroll + randrolls_2


print(roll)
print("Lets play Lucky Sevens:")

while True:

    
    play = input("(R)oll or (Q)uit?: ").lower().strip()

    if play == "q":
        break
    if play != "r":
        print("Invalid Command")
        continue   #goes to beginning of loop
    num = roll()         #IMPORTANT
    if num == 7:
        print("You are lucky")
    else:
        print("You are not lucky")