# match case statements in python: similar to switch case :
# it is similar to switch case but does not need break like in java, python
x=int(input("Enter the value of x:"))
match x:
    case 0:# base case  if x ==0 it will execute
        print("x is 0")
    case _ if x<0:
        print("x is smaller then 0")
    case _ if x>0: # condition
        print("x is greater then 0")
    case _ : # default
        print("x is invalid")
        



