# day 6 : variables and data types
# variables are containers which store some type of data like a int,(number), float(decimal),complex(expresion of complex number),string(chracter sequence)
# data type is which kind of data is present in the  variable in java the type does not need to be explicitly tell before variable creation like java,c++


# primitive
num = 23; # integer
string="saboor" #string
float= 3.42 #float
complex = 3+2j #complex
boolean = True # this can be only true or false only
print(num)
print(string)
print(float)
print(complex)
print(boolean)

# sequencial data type :
#  list , tuple , set , dict
# list = which can contain number if element
# tuple = these are similar to list but we cannot change it
# set =  these are similar to list but no order and no duplicates elements are present 
# dict = this store in a key value pairs

list =[1,2,4];
tuple=(2,4,5,2)
set ={2,4,5,32}
dict={"key":"Value"}
print(list)
print(tuple)
print(set)
print(dict)


# to check type of any variable  we can use type():
print(type(num))
print(type(string))
print(type(float))
print(type(complex))
print(type(boolean))
print(type(list))
print(type(tuple))
print(type(set))
print(type(dict))
