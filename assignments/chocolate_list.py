#author-yaz c

from chocolate_bar import ChocolateBar

def get_candy():
    candy = []

    try:
        with open("assignments/ass-24/chocolate_bars.txt") as file:
            for line in file:
                data = line.split(',')
                title = data[0].strip()
                calories = data[1].strip()
                fat = data[2].strip()
                saturated_fat = data[3].strip()
                protein = data[4].strip()
                carbs = data[5].strip()
                sodium = data[6].strip()
                calcium = data[7].strip()
                nuts = data[8].strip()
                candies = ChocolateBar(title,calories,fat,saturated_fat,protein,carbs,sodium,calcium,nuts)
                candy.append(candies)
    except FileNotFoundError:
    
        print("Sorry")  
    except ValueError:
        print("Sorry the file was not formatted properly")   
    return candy







def display(candy):
    for chocolate_bar in candy:
        candy.display(chocolate_bar)

def get_title():
    for chocolate_bar in candy:
        print(f"-{candy[chocolate_bar]}")
        
candy = get_candy()
#candy = []
# candy.append(ChocolateBar("snickers","273","14g","5g","4.5g","34g","151.5mg","53.5mg",True))
# candy.append(ChocolateBar("rolo","233","10.5g","5.5g","2.5g","34g","83.5mg","65.5mg",False))
# candy.append(ChocolateBar("whatchamacallit","256.5","13","5.5","4.5","30g","116.5","62mg","True"))
# candy.append(ChocolateBar("almond joy","232","14g","8.5g","2.5g","29g","67mg","39.5mg",False))
# candy.append(ChocolateBar("kit kat","220.5","12.5g","7.5g","3g","26.5g","43.5mg","77.5mg",False))
# candy.append(ChocolateBar("m&m","236","10g","6.5g","2g","34g","29.5mg","50.5mg",False))



while True:

    command = input("(L)ist, (S)how Details, (Q)uit: ").strip().lower()

   
    if command == "l":
        for chocolate_bar in candy:
            print(f"-{chocolate_bar.title}")
                
            
                        
    elif command == "s":
        cmmd = input("Which candy? ").strip().lower()
        for chocolate_bar in candy:
            if chocolate_bar.title.lower() == cmmd.lower():
                chocolate_bar.display()
    elif command == "q":
        break
    else:
        print("Invalid Command")