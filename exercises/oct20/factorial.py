#author yaz c


def factorial(num):
    ans = 1
        #send answer to the caller #return will kick one out of a function and if you return something it gives it back
    for i in range (1,num+1):
        ans*=i

    return ans 

result = factorial(5)
print(f"5! = {result}")
