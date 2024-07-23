# functions in python : these are function used too execute certain block of code multiple times we can use def keyword to create function
# 
# 
#
#  

def hello():
    print("hello")

hello()
hello()
hello()
hello()
# here we supply a parameter to a function 
def msg(name):
    print("hello "+name)

msg("saboor")
msg("abdul")


# this message allow
def givemsg(name):
    # this will return a string 
    return ("hello "+name)

x=givemsg("Saboor")
print(x)




def findgreaterNumber(a,b):
    if(a<b):
        return b
    elif(b>a):
        return a
    else:
        print("both are equal")
a=23
b=34

print("the greater Numeber ",findgreaterNumber(a,b))    
print("the greater Numeber ",findgreaterNumber(34,45))    
print("the greater Numeber ",findgreaterNumber(54,2))    
print(findgreaterNumber(2,2))    


# in python : we can also assign a variable with a function
x=findgreaterNumber
print(x(23,4))

# this allow us to make function later if we remove pass it will display error 
def futurefun():
    pass