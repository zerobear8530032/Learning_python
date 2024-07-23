# method of tuple:
tup1=(1,3,5,6,3)
print(tup1)
l=list(tup1)
l.pop()
l[0]=3
tup1=tuple(l)
print(tup1)


# get index of 1 from 1 till 4 :

print(tup1.index(3,1,4))


# print len()
print(len(tup1))