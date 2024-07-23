#  f string is a functionality which allow the user to format string easily:

letter ="hello my name is {} and i am from {}"
name="saboor"
country="india"

# old way of formatting string L
print(letter.format(name,country))
# this will put country first name second
print(letter.format(country,name))
# 
# we can specify which aregument we want first 
letter ="hello my name is {1} and i am from {0}"
print(letter.format(country,name))

# to address this issue where dev need to right so much code and still it is very difficult to maintain so in python 3.6 fstring got introduced
#here is a basic format of fstrinng
# 
# so here the varibale name will come to string ame as country:
print(f"hello my name is {name} and i am from {country}") 
price =4.333333333334
txt = f"this is your price {price:.2f}"
print(txt)

print(f"this can also have exp in it {23+5}")
# we can also use double curly bracket to keep the raw fstring
print(f"hello my name is {{name}} and i am from {{country}}") 