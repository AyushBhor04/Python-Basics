#oops - part 2 
# del keyword
# class Student:
#     def __init__(self,name):
#         self.name=name
# s1= Student("Ayush")
# print(s1.name)  
# del s1
# print(s1.name)           #public attribute

#private(like) attributes and methods
# class Account:
#     def __init__(self,acc_no,acc_pass):
#         self.__acc_no=acc_no              #private attribute
#         self.__acc_pass=acc_pass          #private attribute

#     def reset_pass(self):              #will work since inside class
#         print(self.__acc_pass)
# acc1=Account("12345","abcde")
# # print(acc1.__acc_no)         
# # print(acc1.__acc_pass) 
# print(acc1.reset_pass())

# class Person:
#     __name="Anonymous"

#     def __hello(self):
#         print("Hello person!")

#     def welcome(self):
#         self.__hello()
# p1=Person()
# # print(p1.__name) 
# # print(p1.__hello())          #error as private method
# print(p1.welcome()) 

#Inhertiance
# class Car:
#     color="black"
#     @staticmethod
#     def start():
#         print("car started....")

#     @staticmethod
#     def stop():
#         print("car stopped...")

# class ToyotaCar(Car):
#     def __init__(self,name):
#         self.name=name

# car1=ToyotaCar("Fortuner")
# car2=ToyotaCar("Prius")

# print(car1.name) 
# print(car1.start())           #Single Inhertiance 
# print(car1.color)  

#types of inhertiance
# Multilevel inheritance
# class Car:
    
#     @staticmethod
#     def start():
#         print("car started....")

#     @staticmethod
#     def stop():
#         print("car stopped...")

# class ToyotaCar(Car):
#     def __init__(self,brand):
#         self.brand=brand

# class Fortuner(ToyotaCar):     # Multilevel inheritance
#     def __init__(self,type):
#         self.type=type

# car1=Fortuner("Diesel")
# car1.start()                   # Multilevel inheritance

# Multiple Inheritance
# class A :
#     varA="Welcome to class A"
# class B : 
#     varB = "Welcome to class B"
# class C(A,B):                     # Multiple Inheritance
#     varC="Welcome to class C "

# c1=C()
# print(c1.varC)
# print(c1.varB)                    # Multiple Inheritance
# print(c1.varA)                    # Multiple Inheritance

#Super Method
# class Car:
#     def __init__(self,type):
#         self.type=type
#     @staticmethod
#     def start():
#         print("Car has started ...")
#     @staticmethod
#     def stop():
#         print("Cat stopped")
    
# class ToyotaCar(Car):
#     def __init__(self, name,type):
#         self.name= name
#         super().__init__(type)
#         super().start() 

# car1 = ToyotaCar("Prius","Electrical")
# print(car1.type)

#Class Methods
# class Person:
#     name = "Ananonymous"

#     @classmethod
#     def changeName(cls,name):
#         cls.name=name
# p1=Person()
# p1.changeName("Rahul")
# print(p1.name)
# print(Person.name) 

#public decorator
# class Student:
#     def __init__(self,phy,chem,math):
#         self.phy=phy
#         self.math=math
#         self.chem=chem
#         self.percentage=str((self.phy+self.chem+self.math)/3)+ "%"
    
#     @property
#     def Percentage(self):
#         return str((self.phy+self.chem+self.math)/3)+ "%"
    
# stu1=Student(98,97,99)
# print(stu1.percentage)

# stu1.phy=86
# print(stu1.percentage)  #percentage shoud change here

#Polymorphism
#(implicit overloading of +(operator)) done by python
# print(1+2)  #3 - form 1
# print(type(1))
# print("Apna"+"College") #concatinate - form 2
# print(type("Apna"))
# print([1,2,3]+[4,5,6])  #merge - form 3
# print(type([1,2,3]))

# class Complex:
#     def __init__(self,real,img):
#         self.real=real
#         self.img=img

#     def showNumber(self):
#         print(self.real, "i +", self.img,"j")
    
#     def __add__(self,num2):          #dunder function - uses __
#         newReal=self.real+num2.real
#         newImg=self.img+num2.img
#         return Complex(newReal,newImg)
    
#     def __sub__(self,num2):          #dunder function - uses __
#         newReal=self.real-num2.real
#         newImg=self.img-num2.img
#         return Complex(newReal,newImg)


# num1=Complex(1,3)
# num1.showNumber()

# num2=Complex(4,6)
# num2.showNumber() 

# num3 = num1+num2
# num3.showNumber()

# num3 = num1-num2
# num3.showNumber()

# # define a circle class with radius r using the constructor
# define an Area() method of te class wich calculates area
# and perimeter for the same 

# class Circle:
#     def __init__(self,radius):
#         self.radius=radius

#     def area(self):
#         return (22/7)*self.radius**2
    
#     def perimeter(self):
#         return 2*(22/7)*self.radius

# c1=Circle(21) 
# print(c1.area())
# print(c1.perimeter())  

# define a Employee class with attributes role , department and salary . this class also has a 
# showDetails() methods
# Create a Engineer class that inherits properties from employee and has additional
# attributes name and age
# class Employee:
#     def __init__(self,role,dept,salary):
#         self.role=role
#         self.dept=dept
#         self.salary=salary

#     def showData(self):
#         print("role = ",self.role)
#         print("dept = ",self.dept)
#         print("salaray = ",self.salary)
# class Engineer(Employee):
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         super().__init__("Engineer","IT","75,000")
       
# engg1=Engineer("Ayush","23")
# engg1.showData() 
# e1=Employee("Accountant","Finance","60,000") 
# e1.showData() 

#create a class called order which stores item and price
# use dunder function __get__() to convey that
# order1>order2 if the price of order1>price of order2 
# class Order:
#     def __init__ (self,item,price):
#         self.item=item
#         self.price=price 
#     def __gt__(self,odr2):
#         return self.price>odr2.price

# odr1=Order("Chips","20")
# odr2=Order("tea","15") 

# print(odr1>odr2)   #true