#author-yaz c

import random

def get_scores(): 
    scores=[]
    try:
        with open ("assignments/ass-21/scores.txt") as file:
            for line in file:
                # num = int(line.strip())
                # scores.append()
                # return scores
                if line.strip() != "":
                    scores.append (line.strip())
                
    
    
                
    except FileNotFoundError:
        print("Sorry")
    return scores
    
    
  

def save_scores(scores):
    try:
        with open("assignments/ass-21/scores.txt","w") as file:
            file.write(f"{scores}\n")


    except FileNotFoundError:
        print("Sorry")




def play_round():
    
    play = ("rock","paper","scissors")
    rand_item = random.choice(play)
    
    usr_item = input("(R)ock,(P)aper, or (S)cissors?: ").lower().strip()
    if usr_item == "r":
        usr_item = ("rock")
    elif usr_item == "p":
        usr_item=("paper")
    elif usr_item == "s":
        usr_item = ("scissors")
    print(f"""
    Computer: {rand_item}
    Your Item: {usr_item}""")

    if usr_item == rand_item :
        print("It's A Tie!")
        
        return 0  
    elif usr_item == "rock" > rand_item == "scissors" :
        
        return 1
        
    elif usr_item == "paper" > rand_item == "rock" :
        return 1
    elif usr_item == "scissors" > rand_item == "paper" :
        return 1
    else:
        return -1
       
    
score = get_scores()

while True:
    ans = input("(P) or (Q): ").strip().lower()
    
    if ans == "q":
        
        break
    elif ans != "p":
        print("invalid")
        continue
    
    
    
    if play_round():
                
        
            
        print("Yay")
    
    print(f"The score is {score}")

for scor in score:
    print(scor)
save_scores(score)
