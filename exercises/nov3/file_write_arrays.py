


def save_pets(pets):
    try:
        with open("exercises/nov3/pets.txt","w") as file:
            for pet in pets:
                file.write(f"{pet}\n")


    except FileNotFoundError:
        print("Sorry")


def get_pets():
    pets=[]
    try:
        with open ("exercises/nov3/pets.txt") as file:
            for line in file:
                pets.append(line.strip())
    except FileNotFoundError:
        print("Sorry")
    return pets


my_pets = get_pets()

while True:
    hum = input("(V)iew Pets, (A)dd Pets, (D)elete Pet (Q)uit: ").lower()

    if hum == "v":
        for pet in my_pets:
            print(pet)
    elif hum == "q":
        break
    elif hum == "a":
        hums = input("Enter Pet Name: ")
        my_pets.append(hums)
    elif hum == "d":
        humm = input("Enter Pet Name: ")
        for p in my_pets:
            if p.lower()==pet:

                my_pets.remove(p)
    
        

save_pets(my_pets)


