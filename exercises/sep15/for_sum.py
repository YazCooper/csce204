#author-yaz c

print("I love Math!")

num = int(input("Enter a number between 1 and 10: "))

#number is not in range
if num > 10 or num <1:
    print("Sorry, Invalid input")
else:
    sum=0

    for i in range (num+1):
        sum += i

print(f"sum of 1...{num} = {sum}")

