#Write a python program to print even length words in a string.
def even_words(str):
    get=str.split()
    for word in get:
        if len(word)%2==0:
            print(word)
            str=input("enter the string:\t")
            even_words(str)