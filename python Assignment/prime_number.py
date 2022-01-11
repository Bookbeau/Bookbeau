n=int(input("Enter the Given Number:"))
count=0
for i in range(2,n):
    if n%i==0:
        count=count+1
        break
    if count==0:
        print("The Given Number is prime")
    else:
        print("The given Number is NOt prime")