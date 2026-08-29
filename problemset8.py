# def greatest(a,b,c):
#     if(a>b):
#         if(a>c):
#             print(f"{a} is greatest")
#         else:
#             print(f"{c} is greatest")
#     else:
#         if(b>c):
#             print(f"{b} is greatest")
#         else:
#             print(f"{c} is greatest")
#                OR
    # if(a>b and a>c) 
    # return a
    # elif ....for b and c
    # print(greatest(a,b,c))--->outside function here the return values comes
# a = int(input("enter a number: "))
# b = int(input("enter a number: "))
# c = int(input("enter a number: "))
# greatest(a,b,c)



# def convert(c):
#     return (9*c/5)+32
# c = int(input("enter temperature in celcius: "))
# print(f"temperature in fahrenheit is:{convert(c)}")



# print("hello ",end="")
# print("what is going on")



# def pattern():
#     n=int(input())
#     for i in range(1,n+1):
#         print("*"*n)
#         n-=1

# pattern()
# if through recursion then condition if(n==0):return (this will stop further process)
# we can also write pattern(n-1) after print("*" *n)


# def con(i):
#     return i*2.54
    
# i = int(input("enter any value in inches: "))
# print(f"{i} inch to centimeters is: {con(i)}")



# def table(n):
#     for i in range(1,11):
#         print(f"{n} x {i}={n*i}")

# n=int(input("enter any number: "))
# table(n)


# def list(a):
#     n = []
#     for item in l:
#         # l.remove(a)
#         # return l
#         if not(item == a):
#             n.append(item.strip(a))
#     return n
    
   
# l = ["ankit","kit"]
# print(list("kit"))



# def sm(n):
    
#     if(n==0):
#         return
#     return n*(n+1)/2

# n = int(input("enter any number: "))
# print(f"the sum of the first {n} natural numbers is: {sm(n)}")







# def is_leap(year):
#     if(year%4==0 and (year%100!=0 or year%400==0)):
#         return True
#     else:
#         return False
# year = int(input())
# print(is_leap(year))



# n = int(input("enter any number"))
# l = []
# for i in range(1,n+1):
#    b=i*(i+1)//2
#    l.append(b)
# a = str(l)
# print(a)

# l = [1,2,3]
# a = str(l[0])
# b = str(l[2])
# print(a+b)



# a = int(input())
# l = []
# for i in range(1,a+1):
#     l.append(i)
#     b = str(l[i-1])
#     print(b,end="")
#     # print(str(l[i-1]),end="")
#     # print(i,end="")


    
