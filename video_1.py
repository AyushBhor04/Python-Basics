# # # Print Function
# print("My name is Ayush")
# print("My age is 23")
# print("My name is Ayush","My age is 23")     #, indicates a space
# print(26)
# print(23+40)                                 #treated as numbers
# print("23"+"40")                             #treated as string

#Variables
# name = "Ayush"
# age = 23                                     #Assignment operator-right to left
# price = 25.99   
# age2 = age
# print("name") 
# print(name)
# print(age2) 
# print("My name is :",name)
# print("My age is :",age) 

# Data type 
# print(type(name))
# print(type(age))
# print(type(price))

# age = 23
# old = False
# a = None
# print(type(age))
# print(type(old))
# print(type(a))

# # WAP to add 2 numbers
# a=29
# b=500
# sum = a+b
# print(sum) 

# # Arithematic Operators
# a=5
# b=2
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)   # always returns a float value 
# print(a % b)   # depends on the datatype used and used to give remainder
# print(a ** b)  # a to the power b 

# # Relational Operators
# a = 50 
# b = 20
# print(a==b)
# print(a!=b)
# print(a>=b)
# print(a<=b) 

# Assignment Operators
# num = 10
# num += 20   
# print(num)

# # Logical Operators (Works on boolean variables)
# print(not False)
# print(not True) 
# a=50
# b=30 
# print(not(a>b))
# val1 = True
# val2 = False
# print("AND operator:", val1 and val2)
# print("OR operator:", val1 or val2)
# print("OR operator:", (a==b) or (a>b))   #condition evaluation

# # Type conversion or implicit type conversion 
# a = 2
# b = 4.25
# sum = a + b
# print(sum)        #int converted to float

# c = "2"
# d = 4.25
# sum = c + d       #string cant be added with integer 
# print(sum)

# # Type casting or explicit type conversion 
# a = int("2")
# b = 4.5 
# sum = a + b
# print(sum) 

# a = 3.14
# a = str(a)
# print(type(a)) 

# # Taking input in python 
# name = input("enter  your name :")
# print("Welcome", name)  

# val=input("Enter a value :")
# print(type(val),val)  

# val = int(input("Enter a value :"))
# print(type(val),val)


# name=input("Enter your name :")
# age=int(input("Enter your age :"))
# marks=float(input("Enter your marks :"))

# print("Welcome ", name)
# print("Youre entered age is ", age)
# print("Youre results are ", marks)

# Wap to take two inputs and display their sum 
# print("Enter the 2 values to add") 
# a=int(input("Enter first value :"))
# b=int(input("Enter second value :"))
# sum=a+b
# print("Sum of the given number is :", sum)

# # Wap to input the side of a square and print its area
# side = int(input("Enter the side of the square :")) 
# print("Area of the square with side", side , "is", side**2)

# # Wap to input 2 floating numbers and print their average 
# num_1=float(input("Enter 1st number :"))
# num_2=float(input("Enter 2nd number :"))
# print("Average for the 2 given number is", (num_1+num_2)/2) 

# # Wap to input 2 number a and b 
# # print true if a is greater than or equal to b , if not print false 
# a=int(input("Enter a :"))
# b=int(input("Enter b :"))
# print(a >= b)  