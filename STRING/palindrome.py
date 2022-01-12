#python program to check a string is not pallindrome or not
string=input("enter a string:")
if(string==string[::-1]):
    print("The string is pallindrome")

else:print("The string is not a pallindrome")
    