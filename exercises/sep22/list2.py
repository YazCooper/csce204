#author - yaz c

colors = ["pink","purple","green","orange","black"]

print("Welcome to our color fun program!")



while True:
    clr = input("(V)iew,(A)dd,(R)emove,(Q)uit: ").lower().strip()

    if clr == "q":
        break
    elif clr == "v":
        print("Colors: ")
        for item in colors:
            print(f"{item}")
    elif clr == "a":
        new_color = input("Enter Color: ")
        colors.append(new_color)
        print(f"{new_color} was added.")
    elif clr == "r":
        color = input("Enter Color: ")
        if color in colors:
            colors.remove(color)
            print(f"{color} was removed.")
    else:
        print("Invalid Input")

print("Goodbye")
