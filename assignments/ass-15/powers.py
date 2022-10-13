#author-yaz c


def displayPowers(num):
    answer = 1
    for i in range (0,11):

        

        print(f"{num}^{i} =  {answer}  ")
        answer = answer*num  
        
        

        


while True:
    ask = input("Do you want to (L)ist Powers or (Q)uit?: ")

    if ask == "l":
        num = int(input("Enter Number: "))
        displayPowers(num)
    elif ask == "q":
        break
    else:
        print("Invalid Input")
print("Goodbye!")
