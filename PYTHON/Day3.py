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





# # #-----------------------------------SETS---------------------------------------------
# # """ it has unordered nature you cannot access any element at any time
# #     it is mutable but you can only change hashable values (if set contains 3 against 3 in memory a hash value will be stores and if we add set.add(3) 3 again in that set it will not be added bcz both 3 have the same hashes so 3 is now not hashable)
# #     it cannot have duplicates [1,2,3]
# #     Accessed using methods
# #  """

# # SET = {10,45,32,44}
# # for i in SET:
# #     print(i)
# #     #it will print unordered elements 

# # SET OPERATIONS

# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}

# print(a | b)   # Union         → {1,2,3,4,5,6}
# print(a & b)   # Intersection  → {3,4}
# print(a - b)   # Difference    → {1,2}
# print(a ^ b )  # Symmetric diff→ {1,2,5,6}



# # FOR MORE SET OPERATIONS & SET METHODS
# # GO TO THIS LINK: https://www.w3schools.com/python/python_ref_set.asp




# #-----------------------------------DICTIONARY---------------------------------------------
# """ it has ordered nature you can access any element at any time but not my index but by using keys
#     it is mutable
#     it does not have duplicate
#     Accessed using keys
#  """

# d = {10:11,20:200,30:300,40:400}

# #vanilla python 

# d[50] = 500 #creating a new key value pair 
# print(d[30]) # 300 - Reading a value 
# d[10] = 100 #updating a key value that already exist 


#methods approach :  https://www.w3schools.com/python/python_ref_dictionary.asp
# d = {10:100,20:200,30:300,40:400}


# print(d.get(10))
# print(d.items())
# print(d.keys())
# print(d.values())
# # print(d.pop(20))
# # d.popitem()
# print(d.setdefault(60,3000))


# d.update({70:700})

# print(d)


#traversing (loops) 


# d = {10:100,20:200,30:300,40:400}

# for i in d:
#     print(f"key {i} : value {d[i]}")

#questions

# d1 = {"a":10,"b":20,"c":30} 
# d2 = {"c":40,"d":50,"e":60} 

# for i in d2:
#     d1[i] = d2[i]

# print(d1)



# d1 = {"a":10,"b":20,"c":30} 


# sum = 0 

# for i in d1:
#     sum = sum + d1[i]

# print(sum)

# l = ["a","b","a","c","b","a","c","a","b"]

# d = {}

# for i in l:
#     if i in d.keys():
#         d[i] = d[i] + 1
#     else:
#         d[i] = 1

# print(d)



# d1 = {"a":10,"b":20,"c":30} 
# d2 = {"c":40,"d":50,"e":60} 

# for i in d2:
#     if i in d1.keys():
#         d1[i] = d1[i] + d2[i]
#     else:
#         d1[i] = d2[i]

# print(d1)


#---------------------EXCEPTION / ERROR HANDLING ----------------

# a = 12 

# if a == 12:
#     print("hello")


# a = 10 
# b = int(input("please tell a number :- "))

# print(a/b)

# a = "10"
# b = 5 
# print(a + b)

# num = int("hello")


# a = int(input("please tell your 1st number:-  "))
# b = int(input("please tell your 2nd number:-  "))

# try:
#     print(a/b)
# except Exception as err:
#     print(f"Sorry an error occured as {err}")

# finally:
#     print("if there are errors or there are no errors I will run no matter what ")



# name = input("tell your name :- ")

# print(f"Hello your name is {name}")


# age = int(input("tell your age :- "))

# if age < 18:
#     raise TypeError("you are not eligible")

# print("you are elegible")




#----------------FILE HANDLING-------------------
 # 4 MODES IN FILE r , w , a , x
 # w, a , x can create files 
 # r = Read only (file must exist), w = Write , a = append to end, x = Create (fails if exists)

# open("Hello.txt","x")

# file = open("ABEER.txt", "w")
# data = input("What u want to write in your file: ")
# print(type(data))
# file.write(data)
# file = open("PYTHON/Number_Game_Using_whileLoop.py", "r")

# print(file.read())

# file.close()

with open ("ABEER.txt", "a") as f:
    f.write("" + " I LOVE YOU")