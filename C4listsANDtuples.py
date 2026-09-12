#unlike strings lists are mutable

# LIST OF LIST IS ALLOWED


# friends = ["Apple","Orange",5,345.06,False,"Aakash"]
# print(len(friends))
# print(friends[0])
# friends[0] = "Grapes" 
# print(friends[0])
# print(friends[0:3:2])
# friends.append("VIDHAWANSAK")
# print(friends)
# # append: add at the end

# a = [10,8,1,24,5,63,67,69]
# a.sort() 
# print(a)
# # [1, 5, 8, 10, 24, 63, 67, 69]

# a.reverse()
# print(a)
# # [69, 67, 63, 24, 10, 8, 5, 1]

# a.insert(3,6)
# print(a)
# # [69, 67, 63, 6, 24, 10, 8, 5, 1]

# a.pop(2)
# print(a)
# # [69, 67, 6, 24, 10, 8, 5, 1]
# print(a.pop(2))
# # 6 and changes the list

# print(a)
# # [69, 67, 24, 10, 8, 5, 1]
# a.remove(67)
# print(a)
# # [69, 24, 10, 8, 5, 1]\
# # ask chatgpt for more lists operators


# # TUPLES--->



# # it cant be changed, it is immutable
# # [69, 24, 10, 8, 5, 1]<class 'list'>

# s=(1,4,4,4,2,5,6,8,10)
# # s=()--> empty tuple
# print(s[0])
# # 1
# # s=(1) want to make this tuple so do this -->s=(1,) otherwise it will be int
# # this is tuple with ()
# print(type(s))
 
# d=s.count(4)
# # gives no no. repeats
# print(d)

# e=s.index(4)
# print(e)
# # slicing can also be done in tuple
# # if find in the first it will stop for further
# # chatgpt(tuple)



# fruits = ["apple", "banana", "cherry"]
# x, y, z = fruits

# print(x)
# print(y)
# print(z)


# if we want to print 'hello world' and assign it to the variables then the correct way is: x=y=z="hello world"
# if we want to assign values which are different to the variables the the correct way is: x,y,z=4,5,6



# lists and tuples are indexed

#sorting lists:
# n = int(input("enter the number of elements: "))
# l = []
# for x in range(0,n):
#     q = int(input("enter the numbers: ")) 
#     l.append(q)
# print(l)
# # l.sort()
# # print(l)
# for y in range(n):
#     a=l[y]
#     for z in range(y+1,n):
#         if(l[y]>l[z]):
#             l[y]=l[z]
#             l[z]=a
#             # l[y],l[z]=l[z],l[y]
#         else:
#             continue
# print(l)




#reversing a list:
# x=int(input("enter no of elements: "))
# l=[]
# for y in range(x):
#     q = int(input(f"enter element {y+1}: "))
#     l.append(q)

# print(l)
# # if(x%2==0):
# for i in range(0,x//2):
#     a=l[i]
#     l[i]=l[x-i-1]
#     l[x-i-1]=a
# # else:
# #     for i in range(0,x//2):
# #         a=l[i]
# #         l[i]=l[x-i-1]
# #         l[x-i-1]=a
# print(l)

numbers = (25, 10, 45, 5, 30, 15)

maximum = numbers[0]
minimum = numbers[0]

for num in numbers:
    if num > maximum:
        maximum = num

    if num < minimum:
        minimum = num

print("Tuple:", numbers)
print("Maximum:", maximum)
print("Minimum:", minimum)