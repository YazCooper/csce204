#author-yaz c

print("Let's Count!")

stt = int(input("Enter Starting Number: "))
enn = int(input("Enter Ending Number: "))

count = 0

for i in range (stt,enn +1):
    if i == enn:
        print (i)
    else:
        print (f"{i}, ", end='')
    count = count+1

print(f"There are {count} numbers. ")


