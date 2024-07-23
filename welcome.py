def welcomemsg(name):
    print("welcome !",name)

# so we can say 
if __name__=="__main__":
    welcomemsg("Stranger")
# here if we execute this file from here this will print __main__ if we execute file which improt it then the file name wil print 
print("from welcome",__name__)