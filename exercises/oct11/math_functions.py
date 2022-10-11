#author-yaz c



def factorial(num):
    answer = 1
    for i in range (1, num+1):
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



print("Playing With Numbers!")

###########################################
while True:

    user_ans = input("(F)actorial, (S)um, Sum (R)ange, or (Q)uit: ").strip().lower()
    
    
    
    if user_ans == "q":
        break
    elif user_ans=="f":
        num = int(input("Enter Number: "))
        factorial(num)
    elif user_ans=="s":
        num = int(input("Enter Number: "))
        sum(num)
    elif user_ans=="r":
        num = int(input("Enter Number: "))
        start_num = int(input("Enter Start Number: "))
        end_num = int(input("Enter End Number: "))
        sum_range(start_num,end_num)
    else:
        print("Invalid Input")
print("Goodbye")

    


