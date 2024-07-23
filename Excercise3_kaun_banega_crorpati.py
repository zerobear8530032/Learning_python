# print question like KBC:
# 1 use list data type to store question and their correct answers :
# display the final amount of person taking home after playing the game :
# first lets create question dictionary :
# this will be a dict which will map some questions with answers :
import random 
questions ={1:"Who developed Python Programming Language?",
            2:"Which type of Programming does Python support?",
            3:"Is Python case sensitive when dealing with identifiers?",
            4:"Which of the following is the correct extension of the Python file?",
            5:"Is Python code compiled or interpreted?",
            6:" All keywords in Python are in _________",
            7:"What will be the value of the following Python expression?\n4 + 3 % 5",
            8:" Which of the following is used to define a block of code in Python language?",
            9:"Which keyword is used for function in Python language?",
            10:"Which of the following character is used to give single-line comments in Python?",
            11:"What will be the output of the following Python code? \n i = 1 \nwhile True:\n\tif i%3 == 0:\n\t\tbreak\n\tprint(i)\n\ti + = 1",
            12:"Which of the following functions can help us to find the version of python that we are currently working on?",
            13:"Python supports the creation of anonymous functions at runtime, using a construct called __________",
            14:"What is the order of precedence in python?",
            15:"What will be the output of the following Python code snippet if x=1?\nx<<2",
            16:"What does pip stand for python?",
            17:"Which of the following is true for variable names in Python?",
            18:"What are the values of the following Python expressions?\n2**(3**2)\n(2**3)**2\n2**3**2",
            19:"Which of the following is the truncation division operator in Python?",
            20:"What will be the output of the following Python code? \nl=[1, 0, 2, 0, 'hello', '', []]\nlist(filter(bool, l))"};
options ={1:["Wick van Rossum","Rasmus Lerdorf","Guido van Rossum","Niene Stom"],
          2:["object-oriented programming","structured programming","functional programming","all of the mentioned"],
          3:["no","yes","machine dependent","none of the mentioned"],
          4:[".python",".pl",".py",".p"],
          5:["Python code is both compiled and interpreted","Python code is neither compiled nor interpreted","Python code is only compiled","Python code is only interpreted"],
          6:["Capitalized","lower case","UPPER CASE","None of the mentioned"],
          7:[7,2,4,1],
          8:["Indentation","Key","Brackets","All of the mentioned"],
          9:["Function","def","Fun","Define"],
          10:["//","#","/*","!"],
          11:["1 2 3","error","1 2","none of the mentioned"],
          12:["sys.version(1)","sys.version(0)","sys.version()","sys.version"],
          13:["pi","anonymous","lambda","none of the mentioned"],
          14:["Exponential, Parentheses, Multiplication, Division, Addition, Subtraction","Exponential, Parentheses, Division, Multiplication, Addition, Subtraction","Parentheses, Exponential, Multiplication, Division, Subtraction, Addition","Parentheses, Exponential, Multiplication, Division, Addition, Subtraction"],
          15:[4,2,1,8],
          16:["Pip Installs Python","Pip Installs Packages","Preferred Installer Program","All of the mentioned"],
          17:["underscore and ampersand are the only two special characters allowed","unlimited length","all private members must have leading and trailing underscores","none of the mentioned"],
          18:["512, 64, 512","512, 512, 512","64, 512, 64","64, 64, 64"],
          19:["|","//","/","%"],
          20:["[1, 0, 2, 'hello', ”, []]","Error","[1, 2, 'hello']","[1, 0, 2, 0, 'hello', ”, []]"]}
answers ={1:[3,"Python language is designed by a Dutch programmer Guido van Rossum in the Netherlands"],
          2:[4,"Python is an interpreted programming language, which supports object-oriented, structured, and functional programming"],
          3:[2,"Case is always significant while dealing with identifiers in python"],
          4:[3,"'.py' is the correct extension of the Python file. Python programs can be written in any text editor. To save these programs we need to save in files with file extension '.py'"],
          5:[1,"Many languages have been implemented using both compilers and interpreters, including C, Pascal, and Python"],
          6:[4,"True, False and None are capitalized while the others are in lower case"],
          7:[1,"The order of precedence is: %, +. Hence the expression above, on simplification results in 4 + 3 = 7. Hence the result is 7"],
          8:[1,"In Python, to define a block of code we use indentation. Indentation refers to whitespaces at the beginning of the line"],
          9:[2,"The def keyword is used to create, (or define) a function in python"],
          10:[2,"To write single-line comments in Python use the Hash character (#) at the beginning of the line. It is also called number sign or pound sign. To write multi-line comments, close the text between triple quotes.Example: “”” comment text “””"],
          11:[2,"SyntaxError, there shouldn't be a space between + and = in +="],
          12:[4,"The function sys.version can help us to find the version of python that we are currently working on. It also contains information on the build number and compiler used. For example, 3.5.2, 2.7.3 etc. this function also returns the current date, time, bits etc along with the version"],
          13:[3,"Python supports the creation of anonymous functions (i.e. functions that are not bound to a name) at runtime, using a construct called lambda. Lambda functions are restricted to a single expression. They can be used wherever normal functions can be used"],
          14:[4,"For order of precedence, just remember this PEMDAS (similar to BODMAS)"],
          15:[1,"The binary form of 1 is 0001. The expression x<<2 implies we are performing bitwise left shift on x. This shift yields the value: 0100, which is the binary form of the number 4"],
          16:[2,"pip is a package manager for python. Which is also called Preferred Installer Program"],
          17:[2,"Variable names can be of any length"],
          18:[1,"Expression 1 is evaluated as: 2**9, which is equal to 512. Expression 2 is evaluated as 8**2, which is equal to 64. The last expression is evaluated as 2**(3**2). This is because the associativity of ** operator is from right to left. Hence the result of the third expression is 512"],
          19:[2,"// is the operator for truncation division. It is called so because it returns only the integer part of the quotient, truncating the decimal part. For example: 20//3 = 6"],
          20:[3,"The code shown above returns a new list containing only those elements of the list l which do not amount to zero. Hence the output is: [1, 2, 'hello']"]
        }
usedquestion =set()
def getQuestion():
    """this is a function which will give return a random question form the dataset """
    question=random.randint(1,len(questions))
    while(question in usedquestion):
        question=random.randint(1,len(questions))
        if(len(usedquestion)==len(questions)):
            print("out of questions")
            return 
    usedquestion.add(question)
    print(f"Question {len(usedquestion)} : {questions[question]}")
    print("Options :")
    print(f" 1) {options[question][0]}\n 2) {options[question][1]}\n 3) {options[question][2]}\n 4) {options[question][3]}")
    return question

def getsameQuestion(lookupvalue):
    """this is a function which will give return a random question form the dataset """       
    
    print(f"Question {len(usedquestion)} : {questions[lookupvalue]}")
    print("Options :")
    print(f" 1) {options[lookupvalue][0]}\n 2) {options[lookupvalue][1]}\n 3) {options[lookupvalue][2]}\n 4) {options[lookupvalue][3]}")
    return lookupvalue

def checkanswer(useranswer,lookupvalue):
    try:
        useranswer=int(useranswer)
        if(useranswer<=0 or useranswer>4): 
            raise ValueError   
    except ValueError:
        print("You Need to Enter a Number Between (1-4) ")
        return 
    return (useranswer==answers[lookupvalue][0])

print("welcome to my KBC :")
print("This is a python quiz game which will ask you some python related question ans give you some reward for each correct answers");
print("the question will be shown on the screen and you have to choose one option")
print("just give (1,2,3,4) as answer to ")
playing =True
player_reward =0;
current_reward =1000;
count=0;
lookupvalue=0
skip=False
while(playing or count==len(questions)):
    if not skip:
        lookupvalue =getQuestion()
        count=count+1
    print("CHOOSE ONE OF THE OPTIONS :")
    userinput=input("enter (1,2,3,4)  to choose the option")
    if(checkanswer(userinput,lookupvalue)==True):
        player_reward=player_reward+current_reward
        print("Corrent Answer !!")
        print(f"Your Reward :{player_reward} ")
        current_reward=current_reward*2
        print(f"Next Question worth {current_reward}")
        skip=False
    elif(checkanswer(userinput,lookupvalue)==False):
        print("Wrong Answer !!")
        print("Sorry but you Lost !!")
        print(f"Correct Answer was {answers[lookupvalue][0]}\nExplanation :\n{answers[lookupvalue][1]}")
        if( player_reward==0):
            print("Sorry you does not win any thing")
        else:
            print(f"You got : {player_reward} as a Prize")
            print("Thanks for Playing ")
        playing=False    
        skip=False
    elif(checkanswer(userinput,lookupvalue)==None):
            getsameQuestion(lookupvalue)
            skip=True










