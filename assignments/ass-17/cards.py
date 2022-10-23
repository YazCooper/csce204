#author - yaz c
import random

def deal():

    

    play_one = random.randint(1,10)
    play_two = random.randint(1,10)
    play_three = random.randint(1,10)
    play_four = random.randint(1,10)
    
    
    
    

    print(f"""
    Computer Deals Two Cards: {play_one} and {play_two}
    You Deal Two Cards: {play_three} and {play_four} """)

    comp = play_one + play_two
    usr = play_three + play_four

    if comp == 7:
        print("Computer got the magic 7! They win :( ")
    elif usr== 7:
        print("You Got The Magic 7! You Won This Round!")
    elif comp > usr:
        print("Computer Won This Round!")
    elif comp < usr:
        print("You Won This Round!")
    elif comp == usr:
        
        print("It Was A Tie!")
    
   
        

    
   
    

    


    









print("Card Game")


while True:

    rounds = input("Would you like to play a round? (Y)es or (N)o?: ")
    if rounds == "n": 
       
        break
    else:
        deal()

print("Goodbye!")
        
    
    









