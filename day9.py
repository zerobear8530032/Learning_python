# taking input from user : we can use input("--message--")-> this take input and it takes all input in the form of a string
x=input("enter your name ")
print(x);

# example 
a=input("Enterr a number ")
b=input("Enterr a number ")

print(a," + ",b," = ",(a+b))# here a , b both are string because input convert all input as string 


a=int(input("Enterr a number "))#this can raise error if we enter a string as input 
b=int(input("Enterr a number "))#this can raise error if we enter a string as input 

print(a," + ",b," = ",(a+b))# here a , b both are int  because we type cast the input


