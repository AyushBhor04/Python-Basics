#oops part - 1 

# #creating class
# class Student:
#     name="Karan"

# #creating object
# s1=Student()
# print(s1)
# print(s1.name) 
# s2=Student()
# print(s2.name) #everytme we use name it will print karan as it is used in the blueprint

# class Car:
#     color="blue"
#     brand="Mercedes"

# car1=Car()
# print(car1.color) 
# print(car1.brand) 

#constructor or init function
# class Student:
#     def __init__(self):                           #default constructors
#         pass

#     def __init__(self,name,marks):                #parameterized constructors
#         self.name=name
#         self.marks=marks
#         print(self)                                 #refers to particular instance                           
#         print("Adding new student in database..")
    
# s1=Student("Ayush",98)                               #() - calls the constructors
# print(s1.name,s1.marks)                                    #s1 and self are same 

# s2=Student("Yash",97) 
# print(s2.name,s2.marks)  

#Attributes
# class Student:
#     college_name="Abc college"          #class attributes
#     name="Anonymous"

#     def __init__(self,name,marks):      #object attributes     
#         self.name=name                  #obj attribute>>class attributes
#         self.marks=marks
#         print(self)                                                           
#         print("Adding new student in database..")
    
# s1=Student("Ayush",98)                               
# print(s1.name,s1.marks) 

#Methods
# class Student:
#     college_name="Abc college"
#     def __init__(self,fullname,marks):
#         self.name=fullname
#         self.marks=marks
    
#     def welcome(self):
#         print("Welcome",self.name)

#     def get_marks(self):
#         return self.marks

# s1=Student("Ayush",98)
# s1.welcome() 
# print(s1.get_marks())

#create student class that takes name and marks of 3 subject as arguements in constructor
#then create a method to print the average

# class Student:
#     def __init__(self,name,marks):
#         self.name= name
#         self.marks=marks
    
#     def get_avg(self):
#         sum = 0 
#         for val in self.marks:
#             sum+=val
#         print("Hi",self.name,"your average score is : ",sum/3)
        
# s1 = Student("Ayush",[98,99,96]) 
# s1.get_avg() 

# s1.name="yash"
# s1.get_avg() 

#Static methods
# class Student:
#     def __init__(self,name,marks):
#         self.name= name
#         self.marks=marks
    
#     @staticmethod           #decorator
#     def hello():            
#         print("Hello")

#     def get_avg(self):
#         sum = 0 
#         for val in self.marks:
#             sum+=val
#         print("Hi",self.name,"your average score is : ",sum/3)
        
# s1 = Student("Ayush",[98,99,96]) 
# s1.get_avg() 
# s1.hello() 

#Abstraction
# class Car:
#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.clutch = False

#     def start(self):
#         self.clutch=True
#         self.acc=True
#         print("car started..")
# car1=Car()
# car1.start() 

#create account aclass with 2 attribute - balance and account number
#create method for debit , credit and printng the balance
# class Account:
#     def __init__(self,bal,acc):
#         self.balance=bal
#         self.account_no=acc

#     #debit account
#     def debit(self,amount):
#         self.balance -= amount 
#         print("Rs.",amount,"was debited")
#         print("total balance = ",self.get_balance())
    
#     #credit account
#     def credit(self,amount):
#         self.balance=+ amount 
#         print("Rs.",amount,"was credited")
#         print("total balance = ",self.get_balance())

#     def get_balance(self):
#         return self.balance

# acc1=Account(10000,12345)
# print(acc1.balance)
# print(acc1.account_no) 
# acc1.debit(1000)
# acc1.credit(500)
# acc1.credit(40000)  
# acc1.debit(1000) 