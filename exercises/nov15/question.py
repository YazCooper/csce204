#Author yaz c

class Question:
    def __init__(self,prompt,answer1,answer2,answer3,answer4,correct_answer):
        self.prompt=prompt
        self.correct_answer = correct_answer
        self.answers = (answer1,answer2,answer3,answer4) #a list makes answers easier to call
        
    def display(self):
        for i in range (len(self.answers)):
            print (f"{i+1}. {self.answers[i]}")

    def is_correct(self,answer):
        if answer - 1 == self.correct_answer:
            return True
        else:
            return False
