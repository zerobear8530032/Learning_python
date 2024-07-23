# type casting :type casting a way to change type of data from one data type to another 
# this can be done in 2 ways :
# 1 implicit : this is done automatically by python no data loss possible it does not raise error
# 2 explicit  : this is done by user and data loss is possible and it can raise an error

# explicit type cast 
x=34;
print(x," type ",type(x))
x=float(34)
print(x," type ",type(x))

s="hello"
print(s," type ",type(s))
# s=int("hello") #-> raise an error we cant convert a string character to interger or number 
# print(s," type ",type(s))
num="234"
print(s," type ",type(s))
num=int(num)
print(num," type ",type(num))

# implicit type convertion :
x=2.3
y=3 #-> here y converted to float to divide the number and return the bigggest data type as result 
div =x/y
print(div," type ",type(div))
