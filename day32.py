# methods on sets :
# union (): it is a function which combine 2 sets and give a new set which include items of both set but no duplicates :
set1={1,4,6,31,63,36,3}
set2={7,46,36,63,3,31}
# here we apply union of set 1 and set 2
print("Union ",set1.union(set2))
# so here set1 , set2 does not change at all and a new set is formed by set1 , set 2
# we can chnage it by updatemthod
# this will add all element form set2 in set1 :
# the update will add any iterable object 
set1.update(set2)
print("after update ",set1)
# intersection(): this method will give all element from set 1 which are also present in set 2
# intersection_update():update set 1 to intersection of set 1 and set 2 

print("Intersection ",set1.intersection(set2))
set1.intersection_update(set2)
print("update intersection",set1)

#symetric_difference (): this is a value present in set 1 but  not in set 2 and item present in set2 but not in set 1 :
#symetric_difference_update (): this will update the set 1 with symetric_difference of both sets 
# (a union b) - (a intersect b)
set1 ={2,4,2,2,4,12,4,2,4,2}
set2 ={3 ,5, 3,5,2,42,5,7,4,1,2}
print("simitric diff ",set1.symmetric_difference(set2))



#difference (): this is a value present in set 1 but  not in set 2 :
#difference_update (): this will update the set 1 with difference of both sets 

set1 ={2,4,2,2,4,12,4,2,4,2}
set2 ={3 ,5, 3,5,2,42,5,7,4,1,2}
print(set1.difference(set2))

# issuperset(): this a function which checks wheather the set 1 is a supper set of set 2:
# a super set is a set which contain all element of other set with its own element and every set is a super set of itself
set1 ={2,4,2,2,4,12,4,2,4,2}
set2 ={3 ,5, 3,5,2,42,5,7,4,1,2}
print(set1.issuperset(set1)) #true
print(set1.issuperset(set2)) # false 


# issuperset(): this a function which checks wheather the set 1 is a supper set of set 2 ad return true , false:
# a super set is a set which contain all element of other set with its own element and every set is a super set of itself
set1 ={2,4,2,2,4,12,4,2,4,2}
set2 ={3 ,5, 3,5,2,42,5,7,4,1,2}
print(set1.issuperset(set1)) #true
print(set1.issuperset(set2)) # false 

# issubset(): this a function which checks wheather the set 1 is a sub set of set 2:
# a sub set is a set which contain some element of other set every set is its own sub set :
# completely identical set are also sub sets of each other 
set1 ={1,2,4,5}
set2 ={1,2,4,5,6}
print(set1.issubset(set1)) #true
print(set1.issubset(set2)) # false 

# to add a new element in set 
set1.add(21)
print(set1)

# remove(): it remove the elmenet if present in set other wise raise error 
set1 ={1,5,2,51,21,0,11}
# set1.remove("saboor")
set1.remove(2)
print(set1)


# discardd(): same as remove dont raise error
set1 ={1,5,2,51,21,0,11}
set1.discard("saboor")
set1.discard(2)
print(set1)


# pop (): it removes the last element of set but because set is unorder so it removes a randome element and return the element it poped:
set1={2,5,1,4,51}
print("orignal set",set1)
print("element poped from set 1 :",set1.pop())

print("after pop set",set1)
# del : it deleted the entire set
set1={3,5,31}
del set1 ;
# print(set1)
# clear(): empty the entire set
set1 ={2,4,5}
print("orignal set",set1)
set1.clear()
print("set after clear :",set1)


