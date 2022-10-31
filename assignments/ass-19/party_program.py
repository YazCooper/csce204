#author yaz c


def get_guests():
    guest_book = {}

    with open("assignments/ass-19/guests_list.txt") as file:
        for line in file:
            if line.strip()=="":
                continue
            guests_guess = line.split(",")
            guest = guests_guess[0].strip().lower()
            guesses = guests_guess[1].strip().lower()
            guest_book[guest] = guesses

    return guest_book

def display_guests(guests):
    print("Attending Guest List:")
    for guests in guest_book:
        print(f"-{guests}")

def get_majority_color(guests):
    counter1=0
    counter2=0
    for guests in guest_book:
        if 'pink' in (guest_book[guests]) :
            counter1 +=1
        elif 'blue' in (guest_book[guests]):
            counter2+=1
    if counter1 > counter2:
        print("Most people think you will have a girl!")
    elif counter2 > counter1:
        print("Most people think you are having a boy!")
    elif counter1 == counter2:
        print("There was a Tie!")



        
           
    

        
guest_book = get_guests()


while True:
    get = input("Would You Like To View (G)uest List, (C)olor Winner, or (Q)uit: ").lower().strip()
    if get == "g":
        display_guests(guest_book)
    elif get == "c":
        
        get_majority_color(guest_book)
    elif get == "q":
        break
    else:
        print("Invalid Input")

    