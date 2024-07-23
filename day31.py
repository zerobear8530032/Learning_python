# set : it is a data structure which does not contain any duplicates and it does not have any order and these are very fast to access element :
# we uses {} bracket to create set 
# note but ** when we create and empty set we need to convert it to a set because 
# {}: this is termed as dictonary in python
# sets are unchangable 
# sets are unorder 
# set does not have indexes 
# set does not allow duplicates 
# we can insert different data types

s={1,3,5,3,5,"saboor",34.453}
print(type(s))
print(s)

emptyset ={}# this is treated as dict at first 
print(type(emptyset))
emptyset=set()
print(type(emptyset))


# accessing set items:
for item in s:
    print(item)

