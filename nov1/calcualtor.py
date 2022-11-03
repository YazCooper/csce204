#author-yaz c


def factorial(num):
    answer = 1
    for i in range (1, num + 1):
        answer *= i

    print(f"{num}! = {answer}")

def sum(num):

    answer = 0

    for i in range (1,num+1):
        answer += i

    print(f"Sum of 1 to {num} = {answer}")
#sum numbers from start to finish
def sum_range(start,finish):
    answer = 0

    for i in range (start,finish+1):
        answer += i

    print(f"Sum of {start} to {finish} = {answer}")
def get_int(prompt):
    while True:
        try:
            num = int(input(prompt))
            break
        except ValueError:
            print("Invalid Whole Number")
        return num

def get_float(prompt):
    while True:
        try:
            num = float  (input(prompt))
            break
        except ValueError:
            print("Invalid Decimal Number: ")
        return num

#My program
num = get_int("Enter Number: ")
factorial(num)