# dictionary methods:

emp1={1:100,2:56,3:78,4:30}
emp2={5:31,6:56,7:90}
print(emp1)
print(emp2)
# update (): allow us to add new value to dict 
emp1.update(emp2)
print(emp1)
# li=[2,5,3,53,2]
# update method only take key value pairs
# emp1.update(li);
# print(emp1)


# here wwe convert list to dicts 
l1=[23,3,5,6,32,22]
l2=[3,5,3,25,2,5]

emp1.update(zip(l1,l2))
print(emp1);

# clear(): convert the dict to empty dict
print(emp2)
emp2.clear()
print(emp2)
# pop will remove item which key passed  
print(emp1)
print(emp1.pop(1))
print(emp1)

# popitem(): will remove last element :
print(emp1)
print(emp1.popitem())
print(emp1)

# del : this will delete the entire object

# del emp1
# print(emp1)
# here we can delete emp1 [2] key value
del emp1[2]
print(emp1)