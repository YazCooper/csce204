#author - yaz c



from question import Question

import random

def get_questions():
    questions = []
    #read the questions into the []
    try:
        with open("exercises/nov15/questions.txt") as file:
            for line in file:
                data = line.split(',')
                prompt = data[0].strip()
                answer1 = data[1].strip()
                answer2 = data[2].strip()
                answer3 = data[3].strip()
                answer4 = data[4].strip()
                correct_answer = int(data[5].strip())
                question = Question(prompt,answer1,answer2,answer3,answer4,correct_answer)
                questions.append(question)
    #errors can be stacked
    
    except FileNotFoundError:
    
        print("Sorry")  
    except ValueError:
        print("Sorry the file was not formatted properly")          
    return questions

questions = get_questions()

#main program
score = 0
print("Welcome to our Trivia Game!")

while True:
    command = input("(P)lay or (Q)uit: ").lower().strip()
    

    if command == "q":
        break
  
    question = random.choice(questions)  #random choice from the list called ASK
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
    