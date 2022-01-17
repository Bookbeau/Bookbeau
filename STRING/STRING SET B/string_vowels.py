#write a python program to accept strings which contains all vowels
def CheckString(s):
    s=s.lower()
    vowels=set("aeiou")
    for char in s:
        if char in vowels:
            vowels.remove(char)
        if len(vowels)==0:
            print("Accepted")
        else:print("Not accepted")

s1="Aeiooua"
print(s1)
CheckString(s1)

s2="python"
print(s2)
CheckString(s2)