# String data type in python: the string is a sequence of character which can be assign with single , double or triple double quotes encoded data :

x="saboor"
print(x," type ",type(x))
y='saboor'
print(y," type ",type(y))
z="""saboor"""
print(z," type ",type(z))


# triple quotes : these are mostly use to keep the format of the string :
# example

# the code below will give error because of break line
# x="firstline 
# second line"

x="""first line 
second line 
third line"""

print(x)



# accessing character of string : we can access the character of string by using a index it can be access like an array of chracter 
# here the index is starting from 0 and end with string length-1
# if we exceed the length of an string we will get error

x="hello this is a string"

print(x[3])
# print(x[33])# this will give error

# we can use reverse indexing also in python by using '-' 

print(x[-1])# get the last character of the string""-2 will give second last and so on" 


# looping through a large string :
string ="this is a long string ..."
# here this for loop is like foreach loop in java which take a variable and iterate over its element 
for char in string:
    print(char)


# we can access length of string: using len(string) ->this will return the string length including all blanks spaces 
print(len("hello"))

# 
