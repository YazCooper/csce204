#author yaz c

from unicodedata import name


def get_phone_book():
    phone_book = {}

    #read file and put in phone book
    with open("exercises/oct27/phones.txt") as file:
        for line in file:
            if line.strip()=="":
                continue
            friend_digits = line.split(",")
            friend = friend_digits[0].strip().lower()
            digits = friend_digits[1].strip()
            phone_book[friend] = digits
            



    return phone_book

def display_phone_book(phone_book):
    for name in phone_book:
        print(f"{name} : {phone_book[name]}")


def display_phone_number(phone_book,name):
    if name in phone_book:
        print(f"{name}'s phone number is {phone_book[name]}")
    else:
        print(f"Sorry {name} isn't in our phone book")


phone_book = get_phone_book()
while True:
    get = input("(V)iew,(G)et Number, or (Q)uit: ").lower().strip()
    if get == "q":
        break
    elif get == "v":
        display_phone_book(phone_book)
    elif get == "g":
        name = input("Enter Name: ").strip()
        display_phone_number(phone_book,name)




#display_phone_book(phone_book)

#friends_name=input("Friends Name: ")
#display_phone_number(phone_book,friends_name)



