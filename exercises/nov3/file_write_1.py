#author -yaz c


def get_count():
    try:
        with open("exercises/nov3/count.txt") as file:
            for line in file:
                num=int(line.strip())
                return num
    except FileNotFoundError:
        print("Sorry your file is invalid.")
        return 0
    except ValueError:
        print("Sorry there is not a number in the file")
        return 0

def say_count(num):
    try:
        with open("exercises/nov3/count.txt","w") as file:       # 'w' will overwrite and 'a' will append
            file.write(f"{num}\n")
    except FileNotFoundError:
        print("Sorry your file is invalid.")
        return 0
    
num_glasses=get_count()

print("Lets Drink Water")
while True:
    
    hum = input("(E)nter drinks, (V)iew Today, (Q)uit: ").lower().strip()
    if hum == "e":
        hums=int(input("How many glasses? "))
        num_glasses+=hums
    elif hum == "v":
        print(f"You have drank {num_glasses} glasses of water")
    elif hum == "q":
        break  


say_count(num_glasses)

