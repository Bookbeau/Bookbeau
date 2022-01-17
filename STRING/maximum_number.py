#write a python function to find the max of 3 numbers
def max(a,b,c):
    if(a>b and a>c):
        print("Greater=",a)
    elif(b>a and b>c):
        print("Greater=",b)
    else:
        print("Greater=",c)

a=int(input("Enter no1:"))
b=int(input("Enter no2:"))
c=int(input("Enter no3:"))
max(a,b,c)