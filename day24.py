# tuple in python : a tuple is very similar as list but we cannot change its element we cant add new element to tuple or remove it

# we cant create a single value tuple like this :
tup =(1)
print(tup)
print(type(tup))

# we can create it like this
tup =(1,)
print(tup)
print(type(tup))


tup=(1,2,4,5)
print(tup)
print(type(tup))

# tup[2]=34  # : here we cant make changes in tuple 
print(tup[2])






# Creating Tuples:

# Create a tuple containing the names of five different fruits.
fruits=("mango","apple","banana","cherry","guava")
print(fruits)
# Create a tuple with a single element and verify its type.
# note tup=(1): this is not a tuple its term as integer
singletup=(1,)
print(type(singletup))

# Create a tuple with mixed data types (e.g., a string, a number, and a list).
mixedtuple=(1,2,5,"banana","mango",True,3.53)
print(mixedtuple)


# Accessing Tuple Elements:

# Create a tuple of five integers and print the third element.
inttup=(1,5,6,35,3,6)
print(inttup[2])
# Access the last element of a tuple using negative indexing.
print(inttup[-1])
# Try to change an element of a tuple and observe what happens.
# we cannot change tuple element they are immutable 
# inttup[0]=343

# Unpacking Tuples:

# Create a tuple with three elements and unpack its values into three variables.
tup=(3,6,8)
e1,e2,e3=tup
print(tup)
print(e1,e2,e3)
# Create a tuple with more than three elements and unpack it into three variables using the asterisk (*) operator to capture the remaining elements.
tup=(3,6,8,3,4,2,52)
e1,e2,*e3=tup
print(e1,e2,e3)


# Tuple Operations:

# Create two tuples and concatenate them.

tup1=(2,5,3,5,2,4)
tup2=(3,5,32,5,12)
tup3=tup1+tup2
print(tup3)

# Create a tuple and multiply it by 3.
tup1=(1,3,5,3,5,2)
mul=tuple(i*3 for i in tup1)
print(mul)

# Check if an element exists within a tuple using the in keyword.
print(3 in mul)

# Tuple Methods:

# Create a tuple with repeated elements and use the count method to find the number of times an element appears.
tup=(2,6,3,5,2,6,1)
print(tup.count(2))


# Use the index method to find the position of an element in a tuple.
# note if we use index  and element is not ppresent it will generate error 
print(tup.index(1))


# Nested Tuples:

# Create a nested tuple (a tuple containing other tuples) and access elements from the inner tuples.
nestetup=((1,3,5),(5,3,5))
print(nestetup)
print(nestetup[1][2])
# Modify an element within a mutable element (like a list) inside a tuple.
listtup=([1,2,4,5,2],[2,3,2,5])
print(type(listtup))
listtup[0][1]=34
print(listtup)

# Advanced Tuple Comprehensions:

# Create a list of tuples where each tuple contains a number and its cube for numbers from 1 to 10.
tuplist =[(e,(e*e*e))for e in range(1,11) ]
print(tuplist)
# Given a list of tuples representing student names and their grades, extract the names and grades into separate tuples.
studentdetail=[("zero","A"),("saboor","B"),("zara","A"),("almas","B")]

names,grades= zip(*studentdetail)
print(names)
print(grades)

