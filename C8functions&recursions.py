# def avg():
#     a = int(input("enter any number: "))
#     b = int(input("enter any number: "))
#     c = int(input("enter any number: "))
#     avg = (a+b+c)/3
#     print(avg)
# avg()
# print("yeah")
# def greet():
#     a = input("enter your name: ")
#     print(f"Hello {a}")
# greet()




# FUNCTIONS WITH ARGUMENTS:
# def greet(name,ending):
#     print("Good day,"+name)
#     print(ending)
    
# greet("ABHINAV", "THANKYOU")
# greet("ABHINAV", "THANks")


# def greet(name,ending):
#     print("Good day,"+name)
#     # print(f"Good day {name}")
#     print(ending)
#     return"ok got it?"
# a = greet("abhinav","thankyou")
# print(a)
# def greet(name,ending="thanks")
# print(f"Good day {name}")
# print(ending)



#      RECURSION---------------->>>>>>>>>>>>>>>>>

# def factorial(n):
#     if(n==0 or n==1):
#         return 1
#     return(n*factorial(n-1))
    
# n = int(input("enter any number: "))
# print(f"the factorial of the {n} is: {factorial(n)}")

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * factorial(n - 1)


# n = int(input("Enter a number: "))

# print("Factorial =", factorial(n))

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


n = int(input("Enter number of terms: "))

print("Fibonacci Series:")

for i in range(n):
    print(fibonacci(i), end=" ")