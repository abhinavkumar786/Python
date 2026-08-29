# name=input("enter name:")
# marks=input("enter marks:")
# phone=input("enter phone number:")
# s="The name of the student is {}, his marks are {} and phone number is {}".format(name,marks,phone)
# # PUT EMPTY CURLY BRACKETS WHEN USING FORMAT
# print(s)



# first convert the list into string:
# l=[str(7*i) for i in range(1,11)]
# print(l)
# # for item in l:
# #     print(item)
# # print(list(map(lambda x:print(x),l)))
# s="\n".join(l)
# print(s)




# map() applies your lambda to each element of l.

# Your lambda runs print(x) for each number.

# But print() in Python always returns None.

# So the resulting mapped values are all None.

# When you wrap it in tuple(...), you get a tuple of all those Nones.


# l=(1,2,3,4,5,10,20)
# def div(x):
#     if(x%5==0):
#         return True
# if return x : it means true as it is non zero
#     return False
# print(tuple(filter(div,l)))
# print(list(filter(lambda x:x%5==0,l)))


# from functools import reduce
# l=[1,2,3,4,5,6,7,8,9]
# def greater(a,b):
#     if(a>b):
#         return True
#     return False
# print(reduce(greater,l))

# filter() → expects the function to return True/False (or truthy/falsy) to decide whether to keep each item.

# reduce() → expects the function to return the next accumulated value, not a True/False.

# Step-by-step:

# reduce() starts with first two items: a=1, b=2 → greater(1, 2) → returns False.

# Now reduce() takes that return value (False) as the new a and next item as b=3 → greater(False, 3) → Python converts False to 0 → 0 > 3 → returns False again.

# This keeps going until the end, so final result = False.




# from functools import reduce
# l=[1,2,3,4,5,6,7,8,9]
# def greater(a,b):
#     if(a>b):
#         return a
#     return b
# print(reduce(greater,l))