# #Chapter:1 printing line

# print("Hello, World!")

# #Chapter:2 Comments and Variables

# abeer =  12
# print(abeer)
# """
# --> 3 rules to follow
# 1.var cant start with a no
# 2.no spaces allowed in between var
# 3.no special characters
# --> Naming Conventions in python
# 1.camelCase
# 2.PascalCase
# 3.snake_case
# """
# # Chapter:3 Data Types
# int = -4
# float = 3.4
# # jaisa huma iyota use krte the imaginary value find krne k lia vaisa hi yhan j use hua jo is type ko complex bana rha ha automatically programming ma iyota ki jaga j likhna hota ha 
# complex = 12 +3j 
# string = 'yo bro he said "you are a bad person"'
# boolean_a = True
# boolean_b = False
# n = None # for null values 
# print(type(int))
# print(type(float))
# print(type(complex))
# print(type(string))
# print(type(boolean_a))

# #Slicing of strings
# # a[start:stop:step]
# a = "COLLEGE"
# print(a[0:7:2])
# print(a[::2])    # BY DEFAULT START = 0 AND END = last index + 1 AND STEP = 1

# Question = "Hello How Are You?"
# #How
# print(Question[6:9:1])
# #You
# print(Question[-4:-1:1])
# #Hello
# print(Question[0:5:1])


# Chapter:4 Type Conversion (coverting value from one type to other)
# x = "5"
# y = int(x)
# print(type(x))
# print(type(y))

#following 7 values will always be coverted to false other than that everything is true

#False, 0 , 0.0, "", [],{},()

# Chapther: 5 Input and Output Operators

# name ="Abeer"
# age = 21
# print(f"Hi My Name is {name}, My age is {age}")

# #HOW TO TAKE INPUT
# name = input("What is your name:-")
# age = int(input("What is your age:-"))

# print(f"Hi My Name is {name}, My age is {age}")

# # input always return a string 
# # if you need a number convert it manually by adding int() or float()


#Arithmetic Operators
# There are 7 kinds of operators (+, -, /, //(Floor division), *, **(power operator), %)
# when u need value after div in int then use // and if u need value in float then use /
# Preferences of operators

"""
() - Brackets
** - Exponents (right to left: 2**2**3 = 2**(2**3))
* / // % - Multiplication, Division , Floor Division, Modulus 
+ - - Addition, Subtraction

jo operators ek hi level pr hain un sab ki preference bhi same hi ha jaisa * /
"""


# Comparison Operators
#(==, > , < , <=, >+, !=) return results in bool
# print(16 == 34)
# print(23 != 32)

# Logical Operators
# and, or , not

#Assignment operators (used to assign values to variables)
#(+=, -=, /=, //=(Floor division), *=, **=(power operator), %=)