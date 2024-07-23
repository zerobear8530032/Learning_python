# using for loop with else :
# here the entire loop end at last it execute else 
list =[1,4,5,12]
for x in list:
    print(x)
    
else:
    print("loop end")

# here list was empty because this return list is empty
list =[]
for x in list:
    print(x)
else:
    print(list,"is empty")

# here if loop ended only then else works
for x in range(1,10):
    if(x==4):
        break;
    print(x)
else:
    print("loop ended")

# here also it works same
i=4
while(i>0):
    print(i)
    i=i-1;
else:
    print(i ,"i is  now")