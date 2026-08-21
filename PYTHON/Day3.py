# Functions
# a functions is a reusable block of code which we can use again and again by just calling it's name
# a = 123
# rev = 0
# copy = a

# while a > 0:
#     rev = rev * 10 + a % 10
#     a = a // 10

# if copy == rev:
#     print("Palindrome")
# else:
#     print("Not palindrome")

# converting the exact logic in functions

def palindrome(a):
    rev = 0
    copy = a

    while a > 0:
        rev = rev * 10 + a % 10
        a = a // 10

    if copy == rev:
        print("Palindrome")
    else:
        print("Not palindrome")

n = int(input("Enter number: "))
palindrome(n)