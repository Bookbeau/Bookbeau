#write a python program to remove ith element from string in different ways
#Initializing string
str="Engineering"
print("Original string:"+str)
#removing char at pos 3
#using slice+concatenation
res_str=str[:2]+str[3:]
print("String after removal of character:"+res_str)