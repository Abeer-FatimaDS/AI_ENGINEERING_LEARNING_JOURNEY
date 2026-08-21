# Functions
# a functions is a reusable block of code which we can use again and again by just calling it's name

# Following is primitive approach jis ma hum ek hi var pr kaam krte hain
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


# # following is the functional approach jis ma hum parameers pr kaam krte hain or usse baar baar use krte hian
# def palindrome(a):          # here a is the parameter
#     rev = 0
#     copy = a

#     while a > 0:
#         rev = rev * 10 + a % 10
#         a = a // 10

#     if copy == rev:
#         print("Palindrome")
#     else:
#         print("Not palindrome")

# n = int(input("Enter number: "))
# palindrome(n) # here n is the argument



# # 3 types of argument

# # Positional Argument (u have to provide values against each parmeter and that value will be stored in var in sequence like 1 will be saved in a)

# def mult(a,b,c,d):
#     print(a*b*c*d)

# mult(1,2,59,8)


# # default argument (not necessary to provide all the arguments you can use default values. those default arguments should be at the last like after c if you add any argument like d it will give an error)

# def add(g,h,l=4):
#     print(g+h+l)

# add(1,6)

 


# IN BUILT DATA STRUCTURES IN PYTHON 
# LIST , TUPLE , SET , DICTIONARY


#-----------------------------------LIST---------------------------------------------
""" it has ordered nature you can access any element at any time
    it is mutable (list ma kisi bhi index pr kabhi bhi change kr skte ho)
    it can have duplicates [1,1,2,3,4,4]
    Accessed using indexes
# """
# a = [12,23,43,56,45]
# # print(a)


# # Traversing in list
# # using values

# for i in a:
#     print(i)

# # using index
# for i in range (0,len(a)):
#     print(f"{i}:{a[i]}")



# lst = [3, 1, 4, 1, 5]

# lst.append(9)       # [3,1,4,1,5,9]   — add to end
# print(lst)

# lst.insert(0, 0)    # [0,3,1,4,1,5,9] — insert at index
# print(lst)

# lst.remove(1)       # removes first 1 in this we have to provide value
# print(lst)

# lst.pop()            # removes last element
# print(lst)

# lst.clear()            # removes all element
# print(lst)

# lst.sort()           # sort ascending (for decending add parameter reverse = true)
# print(lst)

# lst.reverse()        # reverse in place
# print(lst)

# len(lst)             # number of items 


# Find the second largest element in a list

# a = [3,7,8,9,11,10]
# largest = a[0]
# sec_largest = a[0]
# for i in a:
#     if i > largest:
#         sec_largest = largest
#         largest = i
#     elif i > sec_largest:
#         sec_largest = i


# print(f"your largest no is {largest}")
# print(f"your Second largest no is {sec_largest}")


# check if list is sorted or not

# a = [1,2,3,4,5,6]

# for i in range(len(a)-1):
#     if a[i] > a[i + 1]:
#         print(f"your list:{a} is not sorted")
#         break
# else:
#     print(f"your list:{a} is sorted")






# #-----------------------------------Tuple---------------------------------------------
# """ it has ordered nature you can access any element at any time
#     it is immutable (A tuple is exactly like a list, except you cannot change it once created)
#     it can have duplicates [1,1,2,3,4,4]
#     Accessed using indexes
#  """

# # 2 Methods in tuple
# t = (1, 2, 3, 2, 1)
# t.index(2)    # → 1  (first position of 2)
# t.count(2)    # → 2  (2 appears twice)


# # Tuple packing

# def students():
#     return "abeer", 21 , "aber@gmail.com"
# info = students()
# print(info)

# name, age, id = info # bcz info is now containing tuple 
# print(f"Name: {name}, Age: {age}, id: {id}")  # tuple unpacking
