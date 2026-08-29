# try:
#     with open('1.txt') as f:
#         print(f.read())
# except Exception as e:
#     print(e)
# try:
#     with open('2.txt') as f:
#         print(f.read())
# except Exception as e:
#     print(e)
# try:
#     with open('3.txt') as f:
#         print(f.read())
# except Exception as e:
#     print(e)
# print("thank you")

# l=[1,2,3,4,5,6,7,8]
# oddlist=[]
# # using enumerate
# for i, item in enumerate(l):

   
#    if(i==2 or i==4 or i==6):
#       oddlist.append(item)
#     # if(index==0):
#     #     continue
#     # if(item%2==0):
#     #     continue
#     # else:
#     #     oddlist.append(item)
# print(oddlist)
    

# a=int(input("enter any number:"))
# l=[a*i for i in range(1,11)]
# print(l)

# try:
#     a=int(input("enter a number:"))
#     b=int(input("enter a number:"))
#     print(a/b)
# except ZeroDivisionError:
#     print("INFINITE")

a=int(input("enter any number:"))
l=[a*i for i in range(1,11)] 
with open("tables.txt","a") as f:
    # f.write(str(l)+"\n")
    f.write(f"Table of {a}:{str(l)}\n")
# write only takes string not the list
    
