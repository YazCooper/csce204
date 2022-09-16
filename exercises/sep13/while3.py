# author-yaz c.

print("Color Party")


while True:
    guess = input("Guess my fav color: ").lower().strip()

    if guess == "purple":
        print("Yay!")
        break    #kicks you out of the loop


    print("Wrong!")

    again = input("Do you want to guess again? (Y)es or (N)o: ").lower().strip()
    if again == "n" or "no":         #no ("Y") if statement because the loop will take one back to the first question of the loop
        break

print("Goodbye!")