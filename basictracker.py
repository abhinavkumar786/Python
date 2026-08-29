# print("------------------SIMPLE CALCULATOR------------------")
# print("enter specific symbols for the operation you want to perform like +,-,*,/")
# sym=input("enter the symbol:")
# a=int(input("enter the number:"))
# b=int(input("enter the number:"))
# c=None
# if(sym=="+"):
#     c=a+b
# elif(sym=="-"):
#     c=a-b
# elif(sym=="*"):
#     c=a*b
# elif(sym=="/"):
#     if(b==0):
#         print("Error:division by 0 is not allowed")

#     else:
#         c=a/b
# else:
#     print("enter valid operations")
#     c=None
# if c is not None:
#     print(f"Result:{c}")
# # NameError: name 'c' is not defined , either intialize c=None or write exit() at exceptional case
# print("------------------ SIMPLE CALCULATOR ------------------")
# print("Choose an operation: +, -, *, /")
# sym = input("Enter the symbol: ")
# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))

# if sym == "+":
#     c = a + b
# elif sym == "-":
#     c = a - b
# elif sym == "*":
#     c = a * b
# elif sym == "/":
#     if b == 0:
#         print("Error: Division by zero is not allowed")
#         exit()  # Stop the program
#     else:
#         c = a / b
# else:
#     print("Invalid operation")
#     exit()

# print(f"Result: {c}")




# Generate multiplication table from 1-10:
# for x in range(1,11):
#     print("\n")
#     table=0
#     for y in range(1,11):
#         print(f"{x}*{y}={x*y}")



# Find length of a list without len():
# a=int(input("no of terms:"))
# l=[]
# c=0
# for i in range(0,a):
#     n=int(input("enter number:"))
#     l.append(n)
# for item in l:
#     c+=1
# print(c)

# M2:using loop and index

# a = int(input("no of terms: "))
# l = []
# for i in range(a):
#     n = int(input("enter number: "))
#     l.append(n)

# count = 0
# i = 0
# try:
#     while True:
#         l[i]   # Access element
#         count += 1
#         i += 1
# except IndexError:
#     pass

# print("Length of the list:", count)

# M3:using recursion

# def list_length(lst):
#     if lst == []:  # Base case: empty list
#         return 0
#     return 1 + list_length(lst[1:])  # Count first element + rest

# a = int(input("no of terms: "))
# l = []
# for i in range(a):
#     n = int(input("enter number: "))
#     l.append(n)

# print("Length of the list:", list_length(l))





# Remove duplicates from a list:
# l=[1,2,2,3,4,5,5]
# b=len(l)
# # for x in list:
# for x in range(b):
#     for y in range(x+1,b):
#     # for y in range(x+1,b):              
#         if l[x]==l[y]:
#             list.remove(l[x])              
#         else:
#             continue
# print(l)
# Modifying the list while iterating over it causes skipping of elements or unexpected behavior.
# The range(x+1, b) is incorrect. x is a list element, not an index.
# Removing elements inside a loop that uses the same list can lead to index errors or logic bugs.


# M2:
# lst = [1, 2, 2, 3, 4, 5, 5]
# lst = list(set(lst))
# print(lst)  # Output might be unordered: [1, 2, 3, 4, 5]

# M3:
# lst = [1, 2, 2, 3, 4, 5, 5]
# unique = []
# for x in lst:
#     if x not in unique:
#         unique.append(x)
# print(unique)  # Output: [1, 2, 3, 4, 5]

# M4:
# lst = [1, 2, 2, 3, 4, 5, 5]
# lst = list(dict.fromkeys(lst))
# print(lst)  # Output: [1, 2, 3, 4, 5]




# Print prime numbers between 1 and N:
a=int(input())



















# # Merge two dictionaries:
# d1={"NAME":"SURNAME",
#     "ABHINAV":"KUMAR"}
# d2={"RAJAT":"SINGH",
#     "ADITYA":"CHAUDHARY"}
# # d1.update(d2)
# # print(d1)
# for key in d2:
#     # ✅ for key in d2 is the same as for key in d2.keys()
#     d1[key]=d2[key]
# print(d1)
# for key, value in d2.items():  d1[key] = value    # also correct

# d1 = {"NAME": "SURNAME", "ABHINAV": "KUMAR"}
# d2 = {"RAJAT": "SINGH", "ADITYA": "CHAUDHARY"}

# merged_dict = {**d1, **d2}
# print(merged_dict)


# 🧠 What does {**d1, **d2} do?
# This is called dictionary unpacking, and it works like this:

# **d1 unpacks all key-value pairs from d1

# **d2 unpacks all key-value pairs from d2

# All those pairs are packed into a new dictionary

# If both dictionaries have the same key, the last one (d2) wins, and its value will overwrite the earlier one.

