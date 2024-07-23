# recursion: it a concept in programming used to solve complex problems it use used by  calling a function with in it self 
# we need to be very carefull while using recursion because it can lead to infinite loops it is not mandatory to use recursion 
# but it is a way to program:
# the most used case of recursion is when traversing trees or graphs :

def factorial (num):
    '''here we implement a factorial of a number using loop'''
    fact =1;
    if(num==0 or num==1):
        return 1
    for x in range(1,num+1):
        fact=fact*x
    return fact

print(factorial(5))
print(factorial(3))
print(factorial(0))


# factorial using recursion:

def factorial(num):
    '''here we implement a function of factorial  using recusion'''
    # here this is base condition
    if(num==0 or num==1):
        return 1
    # here factorial(num-1) is called in its own function
    return num*factorial(num-1)

print(factorial(5))
print(factorial(3))
print(factorial(0))




# create a recursive program to print the fibbonacci series :

def fib(x):
    if(x==0):
        return 0
    if(x==1):
        return 1
    
    return fib(x-1)+fib(x-2)



print(fib(34))



