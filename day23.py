# functions of list in python

l=[23,4,5,25,2]
print(l)
# adding a new element list.append(value): this will add the element at last index
l.append(4)
print(l)
# this will sort the list :
l.sort()
print(l)
# this will reverse the list 
l.reverse()
print(l)
# index will give first oocurence of value generate error if not found :
# print(l.index(32525))
print(l.index(2))
# count number of occurence  of 2 in list
print(l.count(2))
#  here the m contains a reference of a l not a new list is created 
# m=l
# m[0]=3
# print(l)

m=l.copy()
m[0]=3
print(l)
print(m)

# insert allow to insert a element at index :
# it will insert 3 at 1 index
l.insert(1,3)
print(l)


# extends () : this method allow to add a new iterable object with list :
l1=[2,3,4,1,51,2]
l2=[3,4,1,5,124,1]

print(l1)
l1.extend(l2)
print(l1)
l1=[2,3,4,1,51,2]
l2=[3,4,1,5,124,1]

# both did same thing
k=l1+l2
print(k)


