#author yaz c

import random
def get_score():
    try:
        with open("Exercises/nov3/score.txt") as file:
            for line in file:
                num=int(line.strip())
                return num
    except FileNotFoundError:
        print("Sorry")

def save_score(num):
    try:
        with open("exercises/nov3/score.txt","w") as file:
            file.write(f"{num}")
    except FileNotFoundError:
        print("Sorry")


def sum_digits(number):
    sum = 0
    while number>0:
        digit = number % 10
        sum +=digit
        number = number//10








    return sum

def play_round():
    rand_num = random.randint(1000,9999)
    ans = sum_digits(rand_num)
    user_answer = int(input(f"Sum the Digits of {rand_num}"))
    if ans == user_answer:
        print("Yay")
        return True
    else:
        print("Sorry")
        return False

score = get_score()
if play_round():
    score+=1

save_score(score)