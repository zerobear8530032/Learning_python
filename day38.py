# custome error and raise an error:
# we use raise key word to raise an error:
showmsg =True;
n=input("Enter the Number between 5 and 9 ")

if(n.lower()=="quit"):
    showmsg=False
    print("quited")
elif(int(n)<5 or int(n)>9 ):
    raise ValueError("You Enter wrong number")
if(showmsg):
    print("value of n ",n)
