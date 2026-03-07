# #while loop
# count=1           #count is iterator
# while count <= 5:   
#     print("hello")  
#     count += 1
# print(count) 

#print numbers from 1 to 10 
# i = 1 
# while i <= 10:
#     print(i)
#     i+=1

#print numbers from 10 to 1 
# i = 10 
# while i >= 1:
#     print(i)
#     i-=1

#infinite loop 
# while True:
#     print(1)

#print numbers from 1 to 100
# i = 1
# while i <=100: #termination condition
#     print(i)
#     i+=1

#print the numbers from 100 to 1 
# i = 100
# while i >=1:
#     print(i)
#     i-=1 

#print the multiplication table for number n 
# n = int(input("Enter any number :"))
# i=1
# while i<=10 :
#     print(n*i)
#     i+=1

#print the squares of number from 1 to 10 
# i = 1 
# while i<=10:
#     print(i**2)
#     i+=1 

# Print the elements of the following list using loop  
# nums=[1,4,9,16,25,36,49,64,81,100]    
# idx = 0 
# while idx < len(nums): 
#     print(nums[idx])
#     idx+=1

#search for a number x in the tuple using loop
# tup=(1,4,9,16,25,36,49,64,81,100)
# x = int(input("Enter the value to be searched : "))
# idx = 0 
# while idx < len(tup):
#     if(tup[idx]==x):
#         print("Found at index",idx)
#     else:
#         print("Still Finding")     
#     idx+=1  

# i = 1 
# while i <= 5:
#     print(i)
#     if(i==3):
#         break
#     i+=1
# print("End of loop") 

#search for a number x in the tuple using loop and terminate once found
# tup=(1,4,9,16,25,36,49,64,81,100)
# x = int(input("Enter the value to be searched : "))
# idx = 0 
# while idx < len(tup):
#     if(tup[idx]==x):
#         print("Found at index",idx)
#         break                       #breaks the loop
#     else:
#         print("Still Finding")     
#     idx+=1  
# print("End of loop") 

# i = 1 
# while i <= 5:
#     if(i==3):
#         i += 1
#         continue  #skips
#     print(i)
#     i+=1

#print all odd values from 1 to 10
# i = 1 
# while i <= 10:
#     if(i%2==0):
#         i += 1
#         continue  #skips
#     print(i)
#     i+=1

#for loop
# nums = [1,2,3,4,5]
# for val in nums:
#     print(val) 

# veggies = ["Potatoe","Brinjal","Ladyfinger","cucumber"]
# for val in veggies:
#     print(val) 

# tup = (1,2,3,4,2,8,9)
# for num in tup:
#     print (num)

# str = "Ayush Bhor"
# for ch in str: 
#     print (ch)

#for using else(optional and used for break)
# str = "Ayush Bhor"
# for ch in str: 
#     print (ch)
# else:
#     print("end") 

# Print the elements of the following list using for loop  
# nums=[1,4,9,16,25,36,49,64,81,100]    
# for int in nums:
#     print(int) 

#search for a number x in the tuple using loop and terminate once found
# tup=(1,4,9,16,25,36,49,64,81,100)
# x=int(input("enter a number to be searched : "))
# idx=0
# for el in tup:
#     if(el==x):
#         print("Element found at ",idx)
#         break
#     idx += 1 

#range (1 to 5)
# seq=range(5)
# for i in seq:
#     print (i)  
# for i in range(5):
#     print(i) 

# for i in range(2,10):
#     print(i)

# for i in range(2,10,2):
#     print(i) 

#print 1 to 100 using for and range()
# for i in range(1,101):
#     print (i)

#print 100 to 1 using for and range()
# for i in range(100,0,-1):
#     print(i)  

#Print multiplicatin of number n
# n = int(input("Enter any number : ")) #use int else it will take it as string
# for i in range(1,11):
#     print(n*i) 

#pass 
# for i in range(5): 
#                     #error
# print("Some work")
# for i in range(5):
#     pass              #future purposes
# print("Some Work")

# for i in range(5):
#     pass
# if i > 5 :
#     pass
# print("Other work")

#Wap to find the sum of first n natural numbers
# n=int(input("Enter any number : "))
# sum=0
# while n >0 :
#     sum = sum + n
#     n -= 1
# print(sum) 

# n = int(input("Enter any number : "))
# sum = 0 
# for i in range(1,n+1):
#     sum += i
# print(sum) 

#Wap to find the factorial of first n  natural numbers 
# n = int(input("Enter any number : "))
# fact = 1 
# while n > 0 :
#     fact = fact * n
#     n -= 1
# print(fact)  

# n = int(input("Enter any number : "))
# fact = 1 
# for i in range(1,n+1):
#     fact *= i
# print(fact)  
