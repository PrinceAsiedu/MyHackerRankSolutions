# convert a string to int and print it out. 
# if the string is not a number, print out "Bad String".

try:
    a = int(input())
    print(a)
except ValueError:
    print("Bad String")
