# short hand if else:
# it is a technique to write short cut of if else in few lines :
a=0
b=0
if(a>b):
    print("a is greater")
elif(a<b):
    print("b is greater")
else:
    print("both are equal")


# this can be written as :
print("a is greater") if a>b else print("b is greater") if (a<b)  else print("both are equal")

# if you want to do single condition
print("a is greater") if(a>b) else ""

# here we can assign a element :
c=10 if a>b else 0
print(c)