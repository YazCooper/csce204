#author yaz c

FILE_NAME = "exercises/nov10/books.txt"


def write_books(books):
    with open (FILE_NAME, "w") as file:
        for book in books:
            file.write(book + "\n")


def read_books():
    books = []
    with open (FILE_NAME) as file:
        for line in file:
            line = line.replace("\n","") .strip()
            books.append(line)
    return books

def list_books(books):
    for i in range (len(books)):
        print(f"{i+1}. {books[i]}")

def add_books(books):
    book = input("Book: ").strip()
    books.append(book)
    write_books(books)
    print(f"{book} was added.")
    return books

books = read_books() #get books from list

while True:
    command = input("(V)iew,(A)dd, or (Q)uit?: ").strip().lower()

    if command=="q":
        break
    elif command == "v":
        list_books(books)
    elif command == "a":
        books = add_books(books)
    else:
        print("Invalid Command")

write_books(books)
