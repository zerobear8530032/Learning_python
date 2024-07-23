#  The __name__ variable in Python is a special built-in variable that represents the name of the module in which it is used.
#  It is used to check whether a module is being run directly or being imported somewhere else.
#  This allows for code to be executed only when the module is run directly, and not when it is imported.
# here we import a file which contian the welcomemsg function which takes a name 

import welcome
welcome.welcomemsg("abdul saboor")

# so in output there will be 2 msg welcome stranger and welcome name given
# why ? because when ever we import a  particular file in pythonn actually it executes an entire file when it got imported 
# so this could be critical for the programmer if he import some thing and some function fire itself it would be harmful for us
# so tomake sure we does not allow the file to execute any function when we import we use __name__ : this idicate the file
#  is being executed by user or being imported by some one  when we execute
# when ever we execute a file directly the __name__ got __name__ as a value in it so if we execute it here 
# the __name__ will print __main__ but if we use an import from some where else then the file name will be replace with __name__
# means if we execute print(__name__) in welcome and execute from here the welcome will be assign to the __name__
# so we can use this to stop execution of function when we import anything 
print("from day45",__name__)