#author-yaz c


#3!= 1*2*3  (<------Factorial)

def factorial(num):


    answer = 1

    for i in range (1, num+1):      
        answer*=i
        

   

    print(f"{num}! = {answer}")

user_num=int(input("Enter Number: "))
factorial(user_num)