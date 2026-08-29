# sequence of characters enclosed in quotes
# a="abhinav"      single quoted string
# a='abhinav'      double
# a='''abhinav'''  triple
# print(type(a))

# string slicing:string can be sliced for getting a part of the 
# a="abhinav"
# print(len(a))
# b=a[0:3]
# print(b)
# 0:3--> 0,1,2    0:0 gives nothing

# -ve slicing
# convert -ve to +ve index
# print(a[-4:-1]) 
# print(a[3:6]) 
# print(a[1])
# print(a[:4])        0:4
# print(a[0:])        0:7

# slicing with skip value
# print(a[1:4:2])
# [1:4:2]-->it will take the element of index 1 and search and take the other element at an interval of 2 in the range of 4(1,2,3)
#1-->took the element from 1st index and 2-->took element after interval of 2 till the string is finished[1:6:2]-->bia

# print(a.endswith("nav"))
# # if we want to see this,we must include the last letter
# #take care of uppercase letters
# print(a.startswith("abhinav"))

# print(a.capitalize())
# # makes the first letter capital

# count = a.count("a")
# print(count)


# #escape sequence character
# b="courage and valour is truly shown on battlefield\n@abhinav"
# print(b)
# #double quote
# c="courage and valour is truly shown on \"battlefield\""
# print(c)
# Single quote
# d='hey I\'am good'
# print(d)



# x = 5
# y = "John"
# print(x + y)
# error

# y=input("enter the letter that u want to count: ")
# s = "abhinav"
# c=0
# for x in range(0,7):
#     if(y==s[x]):
#         c+=1
#     else:
#         continue
# print(c)
