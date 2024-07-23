# break continue statements in pythons :
# break : the break allow us to exit loop no matter the cndition is true or false:
# continue allow us to skip some iterations:

# this will terminate the loop
for x in range(1,15):
    if x==10:
        break
    print(x*5)

# here when x == 10 it skip the below iteration and start the next iteration
for x in range(1,15):
    if x==10:
        continue
    print(x*5)
