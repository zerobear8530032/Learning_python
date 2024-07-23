# comments are code which are for dev persective which are used to write some statements which are not want to e executed by the compiler

print("hello my name is abdul saboor")
# comment ways :
# 1 . way using #
# 2. way using :(""" --- message --- """)
"""hello this is a commend"""
# escape sequences :
# these are special character sequence which we cannot directly use in sequence so we use some escape character squences

# \n is a escape sequemce will print it in next line
print("hello \nworld ")
# example 2:
# print(" hello my name is  "abdul saboor" ")-> this line will generate error because we cant use "" to print directly 
print(" hello my name is \"abdul saboor\" ");
# print(' hello my name is  'abdul saboor'')-> this line will generate error because we cant use '' to print directly 
print(' hello my name is \'abdul saboor\'');

# parameters of print(sep="string") : this will print the string with given in btw the characters by default sep = " " blank space
print("hello",1,3,sep="-")

# parameters of print(end="string") : this will end  the string with given characters by default end = new line or next line 
print("hello",1,3,end="-")


