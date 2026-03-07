#Functions
# def calc_sum (a,b):        #function definition ; parameters
#     return a+b
# print(calc_sum(3,8))       #function call ; arguements 

# def print_hello():
#     print("hello")

# output=print_hello()
# print(output)         #outprint prints none because func doesnt return anything 

#average of 3 numbers
# def avg(a,b,c):
#     return (a+b+c)/3
# print(avg(92,94,86)) 

# def cal_prod(a=3,b=2): #2 and 3 are default parameters
#     print (a*b)
# cal_prod()            #error if no defualt parameters
# cal_prod(4,8)
# cal_prod(8)          #start giving default parameter from end

#waf to print the length of a list (list is the parameter)
# cities = ["delhi","gurgaon","noida","pune","mumbai","chennai"]
# heroes=["shaktiman","captain america","hulk","thor"]
# #print(len(cities))     #without function
# def print_len(list):
#     print(len(list))
# print_len(cities)
# print_len(heroes)

#waf to print the elements in a single list(list is the parameter)
# cities = ["delhi","gurgaon","noida","pune","mumbai","chennai"]
# heroes=["shaktiman","captain america","hulk","thor"]
# def print_list(list):
#     for item in list:
#         print(item,end=" ")
# print_list(cities)
# print_list(heroes)

#waf to find the factorial of n
# a=int(input("Enter any number : "))
# def fact(num):
#     fact = 1
#     for i in range (1,num+1):
#         fact = fact * i
#     return fact
# x=fact(a) 
# print(x)  

#waf to convert usd to inr , suppose 1usd = 85rs
# usd=int(input("Enter USD to be converted : "))
# def convert(a):
#     return a*85
# inr = convert(usd)
# print(inr) 

#waf to determine if the entered number is odd or even
# num=int(input("Enter a number to be checked : "))
# def check_parity(a):
#     if(a%2==0):
#         print(a,"is even")
#     else:
#         print(a,"is odd")
#     return -1
# check_parity(num) 

#Recursion 
# print form n to 1 using recursion
# def show(n):
#     if(n==0):      #base case (crashes without it)
#         return
#     print(n)
#     show(n-1) 
# show(5)

#Find factorial using recursion
# def fact(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n*fact(n-1)
# x=int(input("Enter the number to find its factorial : "))
# a=fact(x) 
# print(a)                         

#recursive function to calculate sum of first n numbers
# def cal(n):
#     if(n==1):
#         return 1 
#     else:
#         return n + cal(n-1)
# print(cal(5))

#recursive function to print all elements in a list
# cities = ["Mumbai","Andheri","Bandra","Delhi","Chennai"]
# def print_list(list,idx=0):
#     if(idx==len(list)):
#         return
#     print(list[idx])
#     print_list(list,idx+1)
# print(cities)
