# exception handling in pyton: these are special error which allow to catch if any error occur 
# so when that happen every time the program stop execution but we can specify handle it to what to do if it occur:
# try & catch

# here if user input a string we can get errror:

# a=input("Enter the Number");
# try:
#     for i in range(1,11):
#         print(int(a)*i)
# except Exception :
#     print("you enter a string instead of integer")

#     # if an error come this wont run but with try catch it will continue the execution
# print("---rest of code ---------")


# here we can also haandle specific errors :
# try:
#     num=int(input("Enter  a Number"))
# except ValueError:
#     print("You enter wrong input")
# print("code ended")


# we can also handle mutiple errors like having different things to do at different error occurence
l=[1,2,4,6,2,4]
try:
    num=int(input("ENTER A LIST INDEX"))
    print(l[num])
    # this will only fetch index error
except IndexError:
    print("list does not have that index")
    # this will fetch any error 
except ValueError:
    print("Enter wrong input")
except:
    print("some error occured")



