#write a python program words Frequency in string Shorthands
string="This is a Python tutorial"
print(string)

word={key:string.count(key)for key in string.split()}

print("words in the string")
print(word)