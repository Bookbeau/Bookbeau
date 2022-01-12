#Python program to print all prime numbers in an interval
a=int(input("Enter te starting interval:"))
b=int(input("Enter te ending interval:"))
for num in range(a,b+1):
    for x in range(2,num):
        if num%x==0:
            break
        else:
            print(num)
