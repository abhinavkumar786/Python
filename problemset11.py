# class TwoDVector:
#     def __init__(self,i,j):
#         self.i=i
#         self.j=j
        
#     def show(self):
#         print(f"the vector is {self.i}i+{self.j}j")

# class threeDVector(TwoDVector):
#     def __init__(self,i,j,k):
#         super().__init__(i,j)
#         self.k=k
#     def show(self):
#         print(f"the vector is {self.i}i+{self.j}j+{self.k}k")
# a=TwoDVector(1,2)
# a.show()
# b=threeDVector(3,4,5)
# b.show()


# class Animals:
#     classofanimal="animal kingdom"
# class Pets(Animals):
#     pet="pet from animals"
# class Dog(Pets):
#     dogs="dogs from pets"
#     def bark(self):
#         print(f"{self.dogs} barks")
# a=Animals()
# b=Pets()
# c=Dog()
# # c.bark()
# # print(c.dogs)
# # print(c.pet)


# class Employee:
#     salary=38488
#     increment=20
#     @property
#     def salaryafterincrement(self):
#         return (self.salary + self.salary*(self.increment/100))
#     @salaryafterincrement.setter
#     def salaryafterincrement(self,salary):
#         self.increment=((salary/self.salary)-1)*100

#     # new salary=old salary(1+increment/100)

# a=Employee()
# # print(a.salary)
# # print(a.salaryafterincrement())
# # print(a.salaryafterincrement)
# a.salaryafterincrement=1200000
# print(a.increment)
# # With @property: you can access it like an attribute → a.salaryafterincrement.
# Without @property: you must call it like a method → a.salaryafterincrement().
# with these decorators follow above lines and for setter we gave them like =...


# class Complex:
#     def __init__(self,r,i):
#         self.r=r
#         self.i=i
#     def __add__(self,C2):
#         return Complex(self.r+C2.r,self.i+C2.i)
# # without complex:(4,6)
#     def __mul__(self,C2):
#         real = self.r * C2.r - self.i * C2.i
#         imag = self.r * C2.i + self.i * C2.r
#         return Complex(real, imag)
        
#     def __str__(self):
#         return f"{self.r} + {self.i}i"
# a=Complex(1,2)
# b=Complex(3,4)
# print(a+b)
# print(a*b)
