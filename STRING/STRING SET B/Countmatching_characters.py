#write a python program to count the Number of matching characters in a pair of string.
import re
ip1="geeks"
ip2="geeksonly"

c=0
for i in ip1:
    if re.search(i,ip2):
        c=c+1
        print("No. of matching characters are",c)