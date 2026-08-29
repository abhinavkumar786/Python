# class employee:
#     name="abhinav"
#     salary=12000000
#     language="python"
# abhinav=employee()
# print(abhinav.name,abhinav.salary, abhinav.language)
# print(employee.name)
# rohan=employee()
# rohan.name="rohan"
# print(rohan.name,rohan.salary,rohan.language)


# class employee:
#     name="abhinav"
#     salary=12000000
#     language="python"
#     def getinfo(self):
#         print(f"The language is {self.language}.The salary is {self.salary}")
#     @staticmethod#it is decorator, it means there is no use of object ,their data hence no need of writing self
#     def greet():
#         print("Good Morning")


# abhinav=employee()
# print(abhinav.name,abhinav.salary, abhinav.language)
# print(employee.name)
# abhinav.getinfo()# or employee.getinfo(abhinav), it converts into this but above we are not accepting the parameter that's why error
# abhinav.greet()



# class employee:
#     name="abhinav"
#     salary=12000000
#     language="python"
#     def __init__(self):#dunder method which is automatically called
#         print("i am creating an object")
#     def getinfo(self):
#         print(f"The language is {self.language}.The salary is {self.salary}")
# abhinav=employee()
# print(abhinav.name,abhinav.salary, abhinav.language)
# print(employee.name)
# abhinav.getinfo()
# rohan=employee()#again init will print



# class employee:
#     name="abhinav"
#     salary=12000000
#     language="python"
#     def __init__(self,name,salary,language):#dunder method which is automatically called
#         self.name=name
#         self.salary=salary
#         self.language=language    
#         print("i am creating an object")
#     def getinfo(self):
#         print(f"The language is {self.language}.The salary is {self.salary}")
# abhinav=employee("Abhinav Kumar",20000000,"C++")
# # abhinav.name="Abhinav Kumar" no need to write this we can just pass the parameters in init by putting them into calling function
# print(abhinav.name,abhinav.salary, abhinav.language)
# print(employee.name)
# abhinav.getinfo()
