#author-yaz c

todo = []

print("Tasks")

while True:
    lst = input("Do you want to (V)iew, (A)dd,(R)emove, or (Q)uit?: ").lower().strip()

    if lst == "q":
        break
    elif lst == "v":        
        print("Todo list:")
        for item in todo:
            print(f"{item}")
        if len(todo) == 0:
            print(f"Yay! You dont have anything todo.")
        
    elif lst == "a":
        newtd = input("Enter Todo Name: ").lower().strip()
        todo.append(newtd)
        print(f"{newtd} has been added.")
    elif lst == "r":
        nwtd = input("Enter Todo Name: ").lower().strip()
        if nwtd in todo:
            todo.remove(nwtd)
            print(f"{nwtd} has been successfully removed.")
        elif nwtd not in todo:
            print(f"Sorry, {nwtd} is not in your list.")
    else:
        print("Invalid Command")
    

print("Goodbye")

