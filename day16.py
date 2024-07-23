#  loops in python: loops allow to repeate a certain block code to repeatedly execute :
#  for loop : it works for iterate on sequence of iterable objects :
# example:
name="hello"
for i in name:
    print(i)

# while loop: it execute until condition is true :

# i=10
# while(i>=0):
#     print(i)
#     i=i-1


# in range function : it execute 1 till 9 , 10 is excluded

for x in range(1 , 10 ):
    print(x)

# now it will run from 1 till 10 and skip 1 number herer 3 rd parameter  will tell what will be step size
# here 2 represent 1,2,3,4,5,6,7,8,9,10 : and it will print every 2nd element
for x in range(1 , 10,2 ):
    print(x)

for x in range(10,0,-1):
    print(x)


