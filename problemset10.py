# class Programmer:
#     def __init__(self,name,salary,language):
#         self.name=name
#         self.salary=salary
#         self.language=language
    
# n=int(input("enter number of programmers:"))
# l=[]
# for i in range(0,n):
#     print(f"enter details of programmer {i+1}:")
#     name=input("enter name:")
#     salary=int(input("enter salary:"))
#     language=input("enter language:")
#     emp=Programmer(name,salary,language)
#     l.append(emp)
# print("details of programmers:")
# for emp in l:
#     print(f"NAME:{emp.name},SALARY:{emp.salary},LANGUAGE:{emp.language}")
# print(l)
# n=list(map(str,input("enter names continously:").split(),input("enter salary"),input("enter language")))



# names = input("Enter names (space separated): ").split()
# salaries = input("Enter salaries (space separated): ").split()
# languages = input("Enter languages (space separated): ").split()

# n = list(zip(names, salaries, languages))
# print(n)




# a=int(input("enter number:"))
# class Calculator:
#     def __init__(self,a):
#         self.square=a**2
#         self.cube=a**3
#         self.sq_root=a**(1/2)
#     # do by creating methods by def square .....
#     # print(f"the square is {self.n*self.n}")
# then call these functions like a=calculator(4),a.square()...
# # print(a**(1/2))
# calci=Calculator(a)
# print(calci.square,calci.cube,calci.sq_root)

# class Demo:
#     a=2
# o=Demo()
# o.a=0
# print(o.a)
# yes it change the class attribute




# a=int(input("enter number:"))
# class Calculator:
#     def __init__(self,a):
#         self.square=a**2
#         self.cube=a**3
#         self.sq_root=a**(1/2)
#     @staticmethod
#     def greet():
#         print("HELLO")
#     # do by creating methods by def square .....
#     # print(f"the square is {self.n*self.n}")
# # then call these functions like a=calculator(4),a.square()...
# # print(a**(1/2))
# calci=Calculator(a)
# calci.greet()
# print(calci.square,calci.cube,calci.sq_root)


# import random
# class Train:
#     def __init__(self,trainno):
#         self.trainno=trainno
#     def book(self,fro,to):
#         print(f"ticket is booked in train number: {self.trainno} from {fro} to {to}")
#     def getstatus(self):
#         print(f"train no {self.trainno} is running on time")
#     def getfare(self,fro,to):
#         print(f"ticket fair in train no. {self.trainno} from {fro} to {to} is:{random.randint(222,555)}")
# # from random import randint now we use randint directly
# rail=Train(236587)
# rail.book("Nagpur","Delhi")
# rail.getstatus()
# rail.getfare("Nagpur","Delhi")




# class Testing:    
#     def test(slf):
#         print("it works")
#     def anothertest(harry):
#         print("even this works")
# object=Testing()
# object.test()
# object.anothertest()
# we can write slf or any name instead of self but its not a good practice
