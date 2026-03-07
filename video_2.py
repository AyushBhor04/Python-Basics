# str1="This is a string"
# str2='ApnaCollege'
# str3="""This is also a string"""
# str4="This is Apna College's video"

# print(str1)
# print(str2)
# print(str3) 
# print(str4) 

# str5="This is string \nWe are creating in python"
# print(str5)

# str6 = "Apna"
# str7="College"
# final_str=str6+str7
# print(final_str) 
# print(len(final_str)) 
# stra="Ayush"
# strb="Bhor"
# stra_b=stra+" "+strb
# print(stra_b)
# print(len(stra_b)) 

# Indexing
# str="Apna College"
# print(str[0]) 
# ch=str[0]
# print(ch) 
# # #str[4]="@"  gives error , strings cant be manipulated

# # Slicing
# str="Apna college"
# print(str[1:4]) 
# print(str[5:]) 
# print(str[5:len(str)]) 

# # Negative Slicing
# str_Z="Apple"
# print(str_Z[-3:-1]) 

# # String Functions
# str_1="i am studying python from apna college"
# print(str_1.endswith("ege")) 
# print(str_1.capitalize()) 
# print(str_1)                 #no changes in original string 
# str_2=str_1.capitalize()
# print(str_2)                 #original string is modified
# print(str_2.replace("o","a")) 
# print(str_2.replace("python","java")) 
# print(str_1.find("s")) 
# print(str_1.find("from"))
# print(str_1.find("x")) 
# print(str_1.count("o")) 

# # Wap to input users first name and print its length 
# # name=input("Enter your name") 
# # print(len(name)) 

# # Wap to find occurence of $ in a string 
# abc="hello $ , i am $ from india $"
# print(abc.count("$"))  

# light="Pink" 
# if(light=="red"):              # if "true" is used in the condition , it executes everytime 
#     print("Stop")              #indentation - the 4 spaces below the if statement , reason being
# elif(light=="yellow"):         #we dont use brackets here like other programming languages 
#     print("Look")
# elif(light=="green"):
#     print("Go")
# else:
#     print("Light is broken")    

# print("End of code") 

# num=5
# if(num>2):
#     print("Greater than 2")
# if(num>3):
#     print("Greater than 3")  #both are executed here since if

# num=5
# if(num>2):
#     print("Greater than 2")
# elif(num>3):
#     print("Greater than 3")  #only one of the 2 is executed 

# marks=float(input("Enter students marks ")) 
# if(marks>90):
#     print("Grade A")
# elif(marks>=80 and marks<90):
#     print("Grade B")
# elif(marks>=70 and marks<80):
#     print("Grade c")
# else:
#     print("Grade D") 

# age = int(input("Enter your age ")) 
# if(age >= 18):
#     if(age>=65):                                # Nesting 
#         print("You are not eligible to drive")
#     else:
#         print("You are eligible to drive")    
# else:
#     print("You are not eligible to drive") 

#wap to check if the entered number is odd or even
# num=int(input("Enter a number "))
# if(num%2==0):
#     print("Entered number is even")
# else:
#     print("Entered number is odd") 

#wap to find the greatest of all three numbers entered by the user
# a=int(input("Enter number a "))
# b=int(input("Enter number b "))
# c=int(input("Enter number c "))
# if(a>b and a>c):
#     print("a is greatest")
# elif(b>c):
#     print("b is the greatest")     
# else:
#     print("c is the greatest") 

#wap to check if any number is a multiple of 7 or not 
# num=int(input("Enter any number to check its divisiblity by 7 : "))
# if(num%7==0):
#     print("Yes,it is a multiple of 7")
# else:
#     print("No,its not a multiple of 7 ") 

