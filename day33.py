# dictionary is a data structure which allow us to store mutiple item in a single varibale and we can store data in key value pairs
# after python 3.7 they are ordered 

dict ={"saboor":"human","spoon":"object","honeybee":"insect"}
print(dict)
# here is how we cann access vlaue 
print(dict["saboor"])
# we can access element from dictonary very fast :
# but if we use key to access element we need to make sure that key exisits
# print(dict["spike"]) # this is not present in our dict so will give error
# to by pass this problem we cana use 
# get()

print(dict.get("spike"))#here key does not exisit so it give us none

# how to access all keys this will give an iteraable object :
print(dict.keys)
for key in dict.keys():
    print(key,end=" ")
# how to access all values this will give an iteraable object :
print(dict.values)
for value in dict.values():
    print(value,end=" ")
# how to access all values and keys this will give an iteraable object :
print(dict.items())
for key,value in dict.items():
    print(key,":",value,end=" ")
