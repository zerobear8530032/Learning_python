#  enumerate inn python :
# it is a function which give us the index of the element of current iterabe object

marks=[1,5,2,5,2,10,6,5]
index =0;
for mark in marks:
    if(index==3):
        print("this is my marks",mark)
    index+=1
# use enumerate  : 

for index,mark in enumerate(marks):
    if(index==3):
        print("this is my marks",mark)

# here we can use it on the set also
setmarks ={1,2,4,5,16}
for index,mark in enumerate(setmarks):
    if(index==3):
        print("this is my marks",mark)

# we can also specify the starting  index value
setmarks ={1,2,4,5,16}
for index,mark in enumerate(setmarks,start=1):
    print(index,mark)





