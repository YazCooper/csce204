#author-yazmin cooper

print("What Shall We Eat?")


while True:
    eat = input("(B)reakfast, (L)unch, (D)inner, (Q)uit: ").strip().lower()
    if eat == "b" or eat == "breakfast":
        print("We should have eggs")
    elif eat =="l" or eat == "lunch":
        print("We should eat a sandwich")
    elif eat == "d" or eat == "dinner":
        print("We should eat lasagna")
    elif eat =="q" or eat == "quit":
        break
    else:
        print("Invalid Input")

print("Goodbye!")






    

    
    

    

    


    





