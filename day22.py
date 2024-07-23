#  list : in python list is like a dynamic array which allow us to store multiple items in a single variable 

l=[12,4,5,2,5,2] # these list always matain the order
print(type(l))
print(l)

# accesing element from list are using index :it is completely similar to string index
print(l[1])
# iterate over list :
for  item in l:
    print(item)

# we can store mutiple data type in python in a list :
items=["apple","banana",1,3,5]
print(items)

# negative index :
print(items[-1])
print(items[-3]) # just minus with len of list 5-3 = 2 so it will give 2 index value

# in key word this is a keyword allow us to find some value in iterable objects :
print( "a" in "saboor")
print("banana" in items)
print("mango" in items)



# list comprehension :  it allow us to create a list of several element while initializing :
lst =[i*10 for i in range(1,11)] # here we create a lst : which is initalize with i*10 and the value of i is 1 till 11 
print(lst)
 # here we create a lst : which is initalize with i*10 and the value of i is 1 till 11
# we can also put a condition also to create a list  
lst =[i*10 for i in range(1,11) if i%2==0]
print(lst)












# Create and Modify Lists:

# Create a list of your favorite fruits.
fruits =["apple","banana","mango","grapes"]
print("fruit",fruits)
# Add a new fruit to the list.
fruits.append("peach")
fruits.append("guava")
print("After adding new Fruits ",fruits)
# Remove a fruit from the list.
fruits.remove("peach")
print("After removing new Fruit ",fruits)
# Replace one fruit with another.
index=fruits.index("banana")
fruits[index]="leechi"
# fruits.replace("banana","leechi")
print("After replacing a Fruit",fruits)




# Accessing Elements:
# Create a list of numbers from 1 to 10.
numbers =[1,2,3,4,5,6,7,8,9,10]
print(numbers)
# Print the first and last elements.
print("first :",numbers[0]," last element :",numbers[len(numbers)-1])
# Print the elements at index 2 and 4.
print(numbers[2]," ",numbers[4])
# Slicing Lists:

# Create a list of the first 10 letters of the alphabet.
alphabets=['a','b','c','d','e','f','g','h','i','j']
print("alphabet list :",alphabets)
# Slice the list to get the first 5 letters.
print("first 5 letters of list :",alphabets[:5])
# Slice the list to get the last 3 letters.
print("last 3 letters of list :",alphabets[-1:-4:-1])
# Slice the list to get every second letter.
print("Every second letter of List :",alphabets[::2])

# List Operations:

# Create two lists of numbers.
num1=[1,2,4,6,8]
num2=[34,6,2,4]
# Concatenate the two lists.: extends used to add another list too existing list it can take any iterable as a parameter  
concatlist = num1.extend(num2)
print("concatination of lists num1 , num2",concatlist)    
# or 
concatlist = []
for x in num1:
    concatlist.append(x)
for x in num2:
    concatlist.append(x)
print("concatination of lists num1 , num2",concatlist)    
# Multiply the list by 3.
for x in concatlist:
    print(x*3,end=" ")

# List Comprehensions:

# Create a list of the squares of numbers from 1 to 10 using a list comprehension.
numbers =[1,2,3,4,5,6,7,8,9,10]
print("numebers ",numbers)
squarelist=[e*e for e in numbers]
print("square of list items :",squarelist)

# Create a list of even numbers from 1 to 20 using a list comprehension.
evennumbers =[ n for n in range(1,21) if n%2==0]
print(evennumbers)
# Create a list of numbers that are divisible by 3 from 1 to 30 using a list comprehension.
divisibleby3 =[n for n in range(1,31,1) if n%3==0]
print(divisibleby3)

# Using in Keyword:

# Create a list of animals.
animals=["monkey","jaguar","lion","tiger","koala","cat"]
print(animals)
# Check if 'cat' is in the list.
print("cat" in animals )
# Check if 'dog' is in the list.
print("dog" in animals )

# Nested Lists:

# Create a nested list to represent a 3x3 matrix.
matrix =[[1,2,5]
        ,[4,5,1]
        ,[5,7,2]]
print(matrix)
# Access the element at the second row, third column.
print(matrix[1][2])
# Modify the element at the first row, first column.
matrix[0][0]=3
print(matrix)


# Advanced List Comprehensions:

# Create a list of tuples where each tuple contains a number and its square for numbers from 1 to 10.
tuplelist =[(e,e*e) for e in range(1,11)]
print(tuplelist)
# Flatten a nested list using a list comprehension.
matrix =[[1,2,5]
        ,[4,5,1]
        ,[5,7,2]]
print(matrix)
flattenlist =[item for l in matrix for item in l]  
print(flattenlist)


