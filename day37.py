# finally clause: it always executes:
# here 
# try:
#     l=[1,5,2,5]
#     i=int(input("Enter the index"))
#     print("value ",l[i])
# except:
#     print('some error occured')
#     # it always executes :
# # finally:
# #     print("i always executes")
# # this also act as finally here 
# print("i always executes")

# main use of finaaly is in a function
def function():
    try:
        l=[1,5,2,5]
        i=int(input("Enter the index"))
        return l[i]
    except:
        print('some error occured')
        return -1;
        # it always executes :
    finally:
        print("i always executes")
print(function())