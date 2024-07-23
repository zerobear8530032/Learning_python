# if else conditional statements in python :
# these are special statements help us to execute some block of code on the basic of some conditions :

# <,>,<=,=>,==,!= : these are comparating operator which compare 2 values and return  a expression in boolean true or false
age=int(input("Enter your age "));
if(age<18):# the condition is true then  if block will execute
    print("you cannot drive")# this is indented text which is used to distingush a block of code like other languages uses {} python uses a space to use 
else:    # if condition is flase this will execute
    print("you can drive")


# if we want to check mutiple statements we can use elif or multiple elif
# these condition only check statement which will match if non match it excute else by default and if any condition before match the below wont even be checked

a=int(input("Enter a Number"))
if(a==0):
    print("number is 0")
elif(a<0):
    print("number is lesser then 0")
else:
    print("number is lesser then 0")