#A python program to find sum of natural number in an interval
n=int(input("Enter a number:"))
end=int(input("enter ending number:"))
sum=0
temp=n
while temp>0:
    digit=temp%10
    sum+=digit**3
    temp//10
    if n==sum:
        print(n)
        else:print(n,"numbers not armstrong")
