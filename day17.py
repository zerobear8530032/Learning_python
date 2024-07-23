# while loop":it is used to execute a block of code when we dont know whem to stop so we use a condition to execute until it cindition is true :

i =1;
while(i<10):
# this will execute until above condition is true 
    print(i)
    i=i+1
    # the else block execute when while ends or while condition is false
else :
    print("program over")

# emulate do while loop in python:
i=1
while True:
    if(i<=100):
        print(i) 
        break;
    i=i+1


