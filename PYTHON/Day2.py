#Chapter:6 Conditional Statements

# if (12 == 1):
#     print("Hello how are u?")
# elif (12 == 12):
#     print("Pagal ho kya")
# else:
#     print("Go To Hell!!")


# Take input and tell if a person can vote or not

# age = int(input("What is your age? "))
# if (age >= 18):
#     print("You cannot vote")
# else:
#     print("You cannot vote")


# # number is even or odd

# number = int(input("Enter a number: "))

# if (number % 2 == 0):
#     print("No. is even")
# else:
#     print("No. is odd")


# # See if the year is leap year or not 

# year = int(input("Enter Year: "))

# if ((year % 4 ==0) and (year % 400 == 0)):
#     print(f"{year} is a leap year")
# else:
#     print(f"{year} is a century year")


# Chapter:7  LOOPS

# PYTHON HAS 2 TYPES OF LOOPS FOR AND WHILE

# # fOR LOOP MAIN THING FOR Numbers HERE IS RANGE(STARRT, STOP, STEP)
# n = int(input("Enter a number: "))
# for i in range (n,(n*10)+1,n):
#     print(i)

# # For Loop for Strings

# a = "Students"
# lenght = len(a)
# for i in range(lenght ):
#     print(a[i])



# break, continue and else(diff from if else) in loops 
#sTRING rEVERSING

# string = "ABEERA"
# Length = len(string)
# rev = "" # for concatination "a" + "b" = "ab"
# for i in range(Length - 1, -1, -1):
#     rev = rev + string[i]
# print(rev)


# string = "NAMAN"
# Length = len(string)
# rev = "" # for concatination "a" + "b" = "ab"
# for i in range(Length - 1, -1, -1):
#     rev = rev + string[i]
# if rev == string:
#     print("yes it's a palendrome")
# else:
#     print("No it's not a palendrome")
