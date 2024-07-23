#  python import : import in a function which allow us to import any pre install or user define module inside 
# our current file which we are working on 
import pandas as pd 
import math  
# import module * : this will import every single function available on entire module but it can ceate conflits if same name function are present in diffreent files:

# here we import pandas module as name pd
# now we can access its method using its object

# list =[1,4,6,2,5,12]
# # here we use pandas series method to convert list ot a series 
# s=pd.Series(list)
# print(type(s))
# print(s)

print(math.sqrt(24))
print(math.pi)


# dir(): this is a function to check all function properties of all function present in the module:

# print(dir(math))




#  we can import method and functtion , varibale from other files in same directory 
from share import name as n,x as var
n()
print(var)

# here from is used to tell python which file we are using and importing function,variable name 

