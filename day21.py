# real python starts from hhere :
# how many types of functions arguments are present in the functions :
# there are  4 types of arguments we can pass in a function 
# 1 : default argumnets : these aregument pass at the function sign
# 2 : keyword arguments 
# 3 : variable length
# 4 : required arugements


# 1 : default argumnets : these argument pass at the function signature while defining parameters , arguments we pass a 
# default value which is take by default if we does not give any parameter during function call:

# example :

def sum(a=1,b=1): # here we pass a default value of a , b so that if we does not pass anything it will take these by default
    # if we pass argument it will take the passed argument value other wise it will take default value 
    print("sum of ",a," + ",b," = ",(a+b))
sum() # no parameter here both use default values 
sum(5) # with one parameter this will use 5 as a and b will be default 
sum(5,4) # with all parameter this will use 5 as a and 4 as b

# *************************************************:
# note : here are some more case  of such type of arguments:
# **********************************************

# 1 case : is above one where we pass 2 default arguments :
# 2 case : we can do both argument to be non default like 'def sum(a,b):' this is also valid

# 3 case : we can make some argument to be default and some non default like this 

def sum(a,b=1):
    print("sum of ",a," + ",b," = ",(a+b))

# sum() # no parameter here both are not default values so we cant use it like this  
sum(5) # with one parameter this will use 5 as a and b will be default 
sum(5,4) # with all parameter this will use 5 as a and 4 as b

# 4 case : when we want some argument to be default we cant make the first argument default and rest as undefault it will generate error
# def sum(a=1,b): this will generate an error because we already have a =1 so we cant use be undefault
# we can make many un default argument and if we  make one argument default then rest of the argument after that will alsp be default

def sum(a,b=1,c=1):
    # here we have to pass at least 1 argument and max 3 
    print("sum of ",a," + ",b," + ",c," = ",(a+b+c))


# value passing in a function:
def name(fname,mname,lname):
    print("full name :",fname,mname,lname)
# default passing:
name("abdul","saboor","khan")

# when passing value passing it also follow same rule where if we pass a argument name by assigning 
# then we have give all the other parameter name by assigning
# also we have to make sure we does not give any parameter multiple assigniment 
# like this example: name("abdul",fname="saboor",lname="khan")

name("abdul",mname="saboor",lname="khan")# key word argument which allow us to by pass the order of the argument with their argument name 




# 2 required arguments : it is the arguments which we have to pass always it uses where we have to take at least one or multiple argument which are required 
# example :
def division(a,b=1):
    if b==0:
        print("cant divide by 0")
    else:
        print(a," / ",b," = ",(a/b))
# here we can give 2 argument 
division(2,5)
# Here we give only one argument, so b takes its default value of 1
division(5) # we can give one argument 
# division() #invalid   we have to pass at least one argument here 


# 3 variable lemgth atguments also called var args : these are special arguments which are used when the developer does not know
# how many argument will be passed in the funnction
# example : avg of multiple numbers we can take 2 , 3,4 .... mutiple number to take avg wwe cant say how many  element or parameter user will pass 
def avg(*args):# here args is the name of tuple
    print(args)
    s=0
    l=len(args)
    if(l==0):
        l=1

    for x in args:
        s=s+x
    print("avg :",s/l)    

avg(1,3,3,6,1) # here we can pass mutiple arguments and all argument will be passed as a tuple and can be accessed their in function

avg()  # if we pass no parameter this will also works but its not a good practice because it can generate several errors but can be depended on requirement 

# we can see we can pass mutiple argument in var args but we can seperate sum argument from var args like this :
def avg(a, *args):
    s=a
    l=len(args)
    if(l==0):
        l=1
    else:
        l=l+1
    
    for x in args:
        s=s+x
    print("avg :",s/l)    

avg(2,5,5,5,5,5)# now the first argument will be a = 2 and rest of argument will be at  var args 


# note another important point while using var args we cannot use  var args as first element because then rest of element will be part of it
# so we always use them as last parameter when using  or we can use keyword parameters for  using it but not a good practice to use it 
def avg(*args,a):
    s=a
    l=len(args)
    if(l==0):
        l=1
    else:
        l=l+1
    
    for x in args:
        s=s+x
    print("avg :",s/l)    

avg(2,5,5,5,5,5,1,2,3,a=1)# now the first argument at  var args and a =1  

#  4 : keyword arguments : these are special argument which allow us to send the arguements in the form of a dictionary
# dictionary is a data structure uses similar like a hashmap in java which store as key value pairs 

def name(**name): # here we will have a pair ok key values as a dict 
    print(name)
    print(type(name))
    print(name["fname"],name["mname"],name["lname"])



name(fname="abdul",mname="saboor",lname="khan")# here we need to pass all the parameter in a key valuue pairs as a dict where the argumennt name are key and  value will be tthe value of the key 
# these need more care when handling but can be very power full

# name() will give eerror when not handle with care
# we can pass with a normal argument :

def name(msg,**name): # here we will have a pair ok key values as a dict and msg as a single arg 
    print(name)
    print(type(name))
    print(msg, name["fname"],name["mname"],name["lname"])

name("hello !",fname="abdul",mname="saboor",lname="khan")# here we need to pass all the parameter in a key valuue pairs as a dict where the argumennt name are key and  value will be tthe value of the key 
# and hello ! will be as msg 

def name(msg,*args,**name): # when using normal,var args, kwargs we cannot use any other arguments after kwargs except for other kwargs
    print(name)
    print(args)
    print(type(name))
    print(msg, name["fname"],name["mname"],name["lname"])

name("hello !",1,2,3,4,5,fname="abdul",mname="saboor",lname="khan")# here we need to pass all the parameter in a key valuue pairs as a dict where the argumennt name are key and  value will be tthe value of the key 



def example_function(*args, **kwargs):
    print("Positional Arguments:", args)
    print("Keyword Arguments:", kwargs)

# Calling the function with different types of arguments
example_function(1, 2, 3, key1="value1", key2="value2", key3="value3")




# return function allow us to return a value from a function:
def getgreet(name):
    return "hello "+name # this will return the msg 


message=getgreet("saboor")
print(message)


