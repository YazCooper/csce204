#author - yaz c


from question import Question

import random

ask = []

ask.append(Question("What type of animal is a seahorse?","horse","spider","fish","monkey",2))
ask.append(Question("What type of animal is a orangutan?","horse","spider","fish","monkey",3))
ask.append(Question("What type of animal is a daddy long legs?","horse","spider","fish","monkey",1))
ask.append(Question("What type of animal is a foal?","horse","spider","fish","monkey",0))

#main program
score = 0
print("Welcome to our Trivia Game!")

while True:
    command = input("(P)lay or (Q)uit: ").lower().strip()
    

    if command == "q":
        break
  
    question = random.choice(ask)  #random choice from the list called ASK
    print(question.prompt)
    question.display()

    num = int(input("Enter answer number: "))
    #could use try method
    if question.is_correct(num):
        print("Yay")
        score +=1
    else:
        print("Sorry")




print(f"Your score is {score}")
print("Goodbye")
    

    