# class employee:
#     company="ITC Infotech"
#     def show(self):
#         print(f"the name of the employee is {self.name} and the salary is {self.salary}")
    
# # class programmer:
# #     company="ITC Infotech"
# #     def show(self):
# #         print(f"the name of the employee is {self.name} and the salary is {self.salary}")
# #     def showlanguage(self):
# #         print(f"the name is {self.name} and he is good with {self.language} language")
#     # in this we are making a new class with some updates so we have to copy all the reqd data to this class 
#     # that's why we are using inheritance so that it inherit all the info automatically , we just have to add some new info if we want 
#     # just change in the parent class, child class will automatically update itself 

# class programmer(employee):
#     print("it will show first this and then the name")
#     # def show(self):
#     #     print(f"the name of the employee is {self.name} and the salary is {self.salary}")
# a=employee()
# a.name="abhinav"
# a.salary=120000
# a.show()
# b=programmer()
# # b.show()
# print(b.company)#error?/

#see the screenshot for the multiple inheritance
#multilevel inheritance



# class methods:

# class employee:
#     a=1
#     def show(self):
#         print(f"the class value of a is {self.a}")
# e=employee()
# e.a=45
# e.show()
# it will show 45
# but if we want to show the class attribute value then we will use decorator,remove self and write cls

# class employee:
#     a=1
#     @classmethod
#     def show(cls):
#         print(f"the class value of a is {cls.a}")
# e=employee()
# e.a=45
# e.show()
# # value is 1


# property decorators: