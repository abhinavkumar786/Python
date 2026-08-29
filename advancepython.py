# Using walrus operator
# if (n := len([1, 2, 3, 4, 5])) > 3:
#     print(f"List is too long ({n} elements, expected <= 3)")
# Output: List is too long (5 elements, expected <= 3

# type definitions:type hints
# n:int=5
# name:str="abhinav"

# def sum(a:int,b:int)->int:
#     return a+b
# just telling types for convinience

# advance typehints:
# in dict merge them and there should be no repetition:hw
# try except
# try except else:if code runs successfully then the block of else will be executed, also if there is any other code after else that will also be executed
# try except finally:if code runs or not the finally block will execute 
# so there is no differene when writing a code at the last without writing finally
# but it has a difference:when we dealing with the function :if any code contains return (exit after the code runs) and we still want to run any code so we can use finally


# in if __name__==__main__:if we are importing this file in some other file and we do not want that some code to be executed in other file so we use this before that what ever will be in the function that will be executed
# def myfunc():
#     print("hello world!!")
# # myfunc()

# if __name__=="__main__":
#     myfunc()
# # if this code is directly executed by running the file its present in
#     print("we are directly running this code")
#     print(__name__)



# l=[1,2,3,4,5]
# index=0
# for item in l:
#     print(f"the item number at index {index}is {item}")
#     index+=1
# for simplification we will use enumerate function

# for index,item in enumerate(l):
#     print(f"the item number at index {index} is {item}")



# list comprehensions:
# list1 = [1,7,12,11,22]
# list2 = [item for item in list1 if item > 8]
# print(list2)

# mylist=[1,2,3,4,5]
# # squaredlist=[]
# # for item in mylist:
# #     squaredlist.append(item*item)
# # print(squaredlist)
# squaredlist=[item*item for item in mylist]
# print(squaredlist)