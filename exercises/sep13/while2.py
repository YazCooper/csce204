#author-yaz c.

print("Color Party")

color = input("Guess my favorite color: ").strip().lower()


while color != "purple":
    print("Wrong!")
    color = input("Guess Again: ")

print("Yay!")
print("Goodbye!")