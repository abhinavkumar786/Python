# a = 1       #a is an integer
# b = 3
# print(a+b)  #arithmetic operation (=,-,*,/)

# c=2.22      #c is a floating point number
# d=False     #d is a boolean variable (True)
# e="abhinav" #e is a string
# f=None      #f is a none type variable

# g=10-6        #assignment operator
# print(g)      #(=,+=,-=)
# h=10
# h+=6
# print(h)
# i=10
# i/=5
# print(i)
# j=16
# j*=5
# print(j)

# #comparison operator (==,>,<,>=,<=,!=)
# k=5>4
# print(k)
# l=j<k
# print(l)
# m = 5==5
# print(m)
# n=10<=12
# print(n)

# #logical operators(and,or,not)
# #truth table of 'or'
# o=True or False
# print(o)
# p=False or False
# print(p)

# #truth table of 'and'          #multifunction cursor
# print("truth or false is: ",True and False)
# print("truth or false is: ",True and True)
# print("truth or false is: ",False and False)
# print("truth or false is: ",False and True )

# print(not(False ))
# print(not(True))
# u=not False
# print(u)
# print(not(5))

# type casting
# q=24
# q="abhinav"   t=type(q)
# q=24.32

q="31.4"
p=float(q)        
t=type(p)

print(t) 
# print(p)  #-->31.4
# print(type(p))-->float    conversion to which possible ?like c (yes)   5.9 if cast to int then it would be 5 not 6
# inputs

# a=input("enter a number: ")->5
# print("number a is: ",a)          
# b=input("enter a second number: ")->3 
# print("number b is: ",b)
# print(a+b)-->53

#  note:
# Python treats the values as strings, so it concatenates "5" + "3" instead of adding them.
# a=float(input("enter a number: "))
# print("number a is: ",a)          
# b=input("enter a second number: ")
# print("number b is: ",b)
# print("sum is :",a+b)
# one is float and other one is int then the output is float

# one is float/int and other one is string means in normal formatting 
# then the output is error


# x = "awesome"

# def myfunc():
#   x = "fantastic"
#   print("Python is " + x)

# myfunc()

# print("Python is " + x)

# print(5.2+2)
# 7.2


a = 4
b = 3
c = 2

result = a + b * c ** 2 / 2 - 1

print(result)