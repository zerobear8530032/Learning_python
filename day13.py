# methods of string : these are some special functions which are used to apply some function on string whiich are inbuild in python
# note : strings are immutable means we cannnot change the string : every time we apply a function it return a new string original string never changes 


# len()-> return the string length

s="hello"
print(len(s))# return length of string

uppercase =s.upper()# convert all chracter of stirng to upper case but it return a new string object 
# example : we can see both string have different id means these are 2 different object 
print("upper case ",uppercase)
# print(id(s))
# print(id(uppercase))
lowercase=uppercase.lower()# convert entire stirng to lower case 
print("lower case ",lowercase)

# strip: these are method to remove some character from the string :
# strip("string to remove "): this take a parameter to remove the character which are at starting and ending of string no between 
# by default it only removes white space at starting and ending 
string1 ="!! hello ! world !!"
string2 ="            !! hello ! world !!           "
print(string1.strip("!"))# remove ! form starting ending
print(string2.strip())# remove spaces fromt starting and ending 

print(string1.lstrip("!")) # similar but work on left side only
print(string2.lstrip())

print(string1.rstrip("!"))# similar but work on rigth side only
print(string2.rstrip())

# replace(target,replace value ) :take 2 parameters and replace the first parameter with second one and it replace in the entire string 
string =" hi my name is --- ---"
print(string.replace("---","saboor")) # here it will replace all occurrence of "---" with "saboor"

# split():  it split the string input number of chracter list we can pass a parameter to tell where to split the string by default its space:
string = "this is a string "
# not the split chracter will not be included as it act as break point 
print(string.split()) # it will split string into list of string on blanks spaces
print(string.split('a')) # it will split string into list of string on 'a'

print("-------".split('-'))


# capitalize ():convert the string first letter to capital and also convert the rest to lower case :
# note this is used for formating the strings :
string="this is a BLog headING"
print(string.capitalize())

# center():this center the string by adding blanks spaces  or we can add a a parameter to center a string 
# this works by adding some chacter at end and start of string and get to equal length of parameter which are passed 
string ="saboor"
print(string.center(10,"4"))

# count(): it take a parameter and count number of occurence of that in a string:
string ="hello this is a test test string"
print(string.count("test")) 

# startswith(): this check wheather the string starts with the parameter:
# we can also give start, end index to search the result in particular area
string="this string end with name"
print(string.startswith("this"))
print(string.startswith("string"))
print(string.startswith("this",0,6))

# endswith(): this check wheather the string ends with the parameter:
# we can also give start, end index to search the result in particular area
string="this string end with name"
print(string.endswith("name"))
print(string.endswith("string"))
print(string.endswith("s",1,6))

# find(): return the first occurence of the given value :
string="this string end with name"
print(string.find("i"))
print(string.find("strings")) # if not found return -1
print(string.find("i",6,10)) # we can pass index to limit the seach 

# index(): return the first occurence of the given value :
string="this string end with name"
print(string.index("i"))
# print(string.index("strings")) # if not found generate error 
print(string.index("i",6,10)) # we can pass index to limit the seach 

# isalnum(): return true if a stirng contain alphabets or numerical character  return false if it contain special symbols also
string ="123assf"
print(string.isalnum()) # true
print("hello".isalnum()) # true
print("35".isalnum()) # true
print("35#$".isalnum()) # false

# isnum(): return true if a stirng contain alphabets   return false if it contain special symbols also
string ="123assf"
print(string.isalpha()) # true
print("hello".isalpha()) # true
print("35".isalpha()) # true
print("35#$".isalpha()) # false




# islower(): checks the entire string is in lower :
string ="hell12o"
print(string.islower())
print("String".islower())

# isupper(): checks the entire string is in upper  :
string ="hello"
print(string.isupper())
print("String".isupper())
print("HELLO".isupper())


# isprintable():returns true if  the entire chracter is printable
string = "print"
print(string.isprintable())
print("string\n".isprintable())


# isspace(): return the  true if their are only spaces in a string  :
string ="    "
print(string.isspace())
print("   hello  ".isspace())


# istitle(): checks the string where each word first letter is a in upper case :
string =" hello this is  a title";
print("String Is A Title".istitle())
print(string.istitle())

# title(): converts string to title case  string where each word first letter is a in upper case :
string =" hello this is  a title";
print(string.title())

# swapcase (): convert the lower case to upper case and upper case to lower case :

string ="Case"
print(string.swapcase())