#author yaz c


def list_friends():
    friends=[]

    with open("exercises/oct25/friends.txt") as file:                    #could name file anything "as ___"
        for line in file:                                      
            friend = line.strip()
            friends.append(friend)
        
        


    return friends


people = list_friends()

print("Party Time")

while True:
    choose = input("(C)heck Guests, (L)ist Guests, (Q)uit: ").strip().lower()

    if choose == "l":
        for person in people:
            print(f"-{person}")
    elif choose == "c":
        chose = input("Enter Name: ")
        if chose in people:
            print(f"{chose} is on the list")
        else:
            print(f"Sorry, {chose} is not on the list.")
    elif choose == "q":
        break
        
