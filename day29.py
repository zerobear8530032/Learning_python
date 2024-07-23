# doc string , pep 8:
# doc string is a literal appear just after the function class or module:
# doc strings are a type of description which we give to a function or class which we can also access later 
# these are not like comments they does not show when we create them but they still remains their and can be access with attribute __doc__

def square(x):
    # we can see the doc string use '''''' quotes to initialize 
    '''this function take one number as input and return its square'''
    return x**2

print(square(5))
# access doc string
print(square.__doc__)


def square(x):
    # we cant create doc string any where it needs to be in the top part of the function or class  
    print("square is ")
    '''this function take one number as input and return its square'''
    return x**2

print(square(5))
# access doc string : this will show None

print(square.__doc__)

