# a = int(input("enter a number: "))
# i=1
# while(i<=10):
#     z = a*i
#     i+=1
#     print(z)
#                  OR
# for i in range(1,11):
#     print(f"{a} x {i} = {a * i}")
# write print statement in while




# l = ["Harry", "Soham", "Sachin", "Rahul"]
# x,y,z,a = l
# print(f"good evening {x}")
# for name in l:
#     if(name.startswith("S")):
#         print(f"Hello {name}")



# a = int(input("enter any number: "))
# i = 1
# count = 0
# while(i<=a):
#     if(a%i==0):
#         count+=1
#     i+=1
# if(count==2):
#     print(f"{a} is a prime nnumber")
# else:
#     print("not a prime number")

# for i in range(2,a):
#     if(a%i==0):
#         print("not a prime number")
#         break
# else:
#     print("prime number")
    # what if we place break in for instead of if?



# SUM OF N NUMBERS:
# n = int(input("enter any number: "))
# i = 1
# s=0
# while(i<=n):
#     s+=i
#     i+=1
# print(s)  
#                  OR
# sum = 0
# for i in range(1,(n+1)):
  
#     sum+=i
#     # i+=1
# print(sum)





# n = int(input("enter any number: "))
# fact = 1
# for i in range(1,n+1):
     
#      fact = fact*n
# # fact = fact*i
#      n-=1
#     #  if(n==0):
        # break (not reqd)
# print(fact)




# PATTERNS------->>>>>


# n = int(input("enter any number: "))
# for i in range(1,n+1):
#     print(" "* (n-i), end="")
#     print("*"* (2*i-1), end="")
#     print("")


# By default, print() moves to a new line after printing, but when you use end="", it prevents that line break, allowing multiple print statements to continue on the same line.

# first check how many lines of stars
# then see the gap before the stars
# number of stars(even or odd)
# make use of end and the last print




# n = int(input("enter any number: "))
# for i in range(1,n+1):
#     print("*"*i)
    # print("")





# n = int(input("enter any number: "))
# for i in range(1,n+1):
#     if(i==1 or i==3):
#         print("*"*n)
#     else:
#         print("*",end="")
#         print(" ",end="")
#         print("*")




# a = int(input("enter a number: "))
# i=10
# while(i>=1):
#     if(i==0):
#         break
#     print(f"{a} x {i}={a*i}")
#     i-=1
#             OR

# for i in range(1,11):
#     print(f"{a} x {11-i} = {a * (11-i)}")







# factorial of a number
# x = int(input("enter a number: "))
# a=x
# fact = 1
# for i in range(1,x+1):
#     fact = fact*(a)
#     a-=1
# print(fact)


# x = int(input("enter a number: "))
# i=x
# fact=1
# while(i>0):
#     fact=fact*i
#     i-=1
# print(fact)

# sum of n numbers
# x=int(input("enter a number: "))
# sum=0
# for i in range(1,x+1):
#     sum=sum+i
# print(sum)



# fibonacci series
# x = int(input("enter the no. of terms: "))
# for i in range(0,x):
#     if(i==0):
#         a=0
#         print(a)
#     elif(i==1):
#         b=1
#         print(b)
#     else:
#         c=a+b
#         a=b
#         b=c
#         print(c)



# PALINDROME:

# STRING palindrome:
# with loop
# n = (input("enter any word to check whether it is palindrome or not: "))
# x=len(n)
# for i in range(x//2):
#     if n[i]!=n[x-i-1]:
#         print("it's not  a palindrome")
#         break
#     # else:
# else:
#     print("it's a palindrome")
        

# with slicing(string):
# n = (input("enter any word to check whether it is palindrome or not: "))
# x=len(n)
# if n==n[::-1]:
#     print("it's a palindrome")
# else:
#     print("it's not a palindrome")


# x=print(5)
# print(x) #print 5 and none



# NUMBER PALINDROME:

# def is_palindrome(num):
#     original = num
#     reverse=0
#     while(num>0):
#         digit=num%10
#         reverse=reverse*10+digit
#         num//=10
#     return original==reverse
# x=int(input("enter any number: "))
# if is_palindrome(x):
#     print(f"{x} is a palindrome")
# else:
#     print(f"{x} is not a palindrome")







# ADVANCE:

# STUDY THIS IN DETAIL AFTERWARDS!!!!!!!!!

# Palindrome Check Ignoring Case & Spaces
# def is_palindrome_advanced(text):
#     # Convert to lowercase and remove spaces
#     cleaned = "".join(ch.lower() for ch in text if ch.isalnum())
#     return cleaned == cleaned[::-1]

# # Test
# user_input = input("Enter a string or sentence: ")

# if is_palindrome_advanced(user_input):
#     print("Palindrome")
# else:
#     print("Not a palindrome")
# ✔ How it works:
# ch.isalnum() → Keeps only letters and digits (ignores spaces, punctuation).

# .lower() → Converts everything to lowercase.

# Compare cleaned text with its reverse.

# ✅ Example Runs

# Input: A man a plan a canal Panama → Palindrome

# Input: No lemon, no melon → Palindrome

# Input: Hello → Not a palindrome




# COUNT THE NO OF DIGITS AND THEIR SUM AND ARMSTRONG NUMBER:


# x= int(input("enter a number: "))
# def digits(num):
#     original = num
#     SUM=0
#     sum=0
#     count=0
#     while(num>0):
#         digit = num%10
#         num//=10
#         count+=1
#         SUM=SUM+digit
#         sum=sum+(digit**3)
#     return count,SUM,original==sum
# count, SUM,sum = digits(x)  # Unpack the returned tuple

# # print("Number of digits in the given number:",digits(x))----->Number of digits in the given number: (3, 4)<-------


# print("Number of digits in the given number:",count)
# print("sum of digits is:",SUM)
# # if sum==0:
# #     print("enter valid number")????????????????????????????????
# if sum:
#     print(f"{x} is armstrong")
# else:
#     print(f"{x} is not armstrong")

# SUM is a local variable inside the function digits(), not outside.
# Local variables cannot be accessed outside the function unless you return them.
# digits(x) returns (count, SUM) as a tuple.

# count and SUM outside the function are new variables created when unpacking that tuple.
# They are not the same variables as the ones inside the function, but they have the same values.
# digits(x) returns a tuple (count_value, SUM_value)
