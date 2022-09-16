#author-yaz c.




hello = input("Do you want me to say hello (Y)es or (N)o: ").strip().lower()

while hello == "y":
    print("Hello")
    hello = input("Do you want to say hello again? (Y)es or (N)o: ").lower().strip()

print("Bye for now")

