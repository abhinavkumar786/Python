# n = int(input("total orders: "))
# l = []
# l2 = []
# for i in range(1,n+1):
#     print("order number: ")
#     on = int(input())
#     l.append(on)
# print(l)
# c=0

# k = int(input("display order: "))
# if(k>n):
#     print("error as order display cant be greater than the total orders")
# else:
#     for x in range(0,k):
#         l2.append(l[x])
# print(l2)
# y=k
# for z in range(0,n-k): 
#     # y=k
#     for j in range(0,k):
#         if(l2[j]>0):
#             c+=1
#             if(c==k):
#                 print(0)
#                 break
#             # else:
#             #     break
#             # print("number set of three is not negative")
#         if(y>=n):
#             # print(l2[j])
#             break
#         else:
#             if(j==1):
#                 j-=1
#             if(j==2):
#                 j-=2
#             print(l2[j])
#             l2.remove(l2[j])
#             l2.append(l[y])
#             y+=1
#             print(l2)
        
# # if(c==k):
# #     print(0)
# # may be correct
# # change some approach by seeing revised code



# from advancepython import myfunc
