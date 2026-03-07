# marks1=94.4
# marks2=87.5
# marks3=95.2
# marks4=66.4
# marks5=45.1
# # or
# marks = [94.4 , 87.5 , 95.2 , 66.4 , 45.1] #list
# print(marks)
# print(type(marks))       #type
# print(marks[0])          #indexing
# print(marks[3])

# student=["Karan", 95.4,17,"Delhi"] #heterogenous list
# print(student) 
# student[0]="arjun"
# print(student)         #mutable nature of lists
# # str = "hello"
# # print(str[0])
# # str[0]="y"           #immutable nature of string  

#list slicing
# marks = [94.4 , 87.5 , 95.2 , 66.4 , 45.1] 
# print(marks[1:4])
# print(marks[:4])
# print(marks[1:])
# print(marks[-3:-1])     #negative indexing

#list methods
# list = [2,1,3]
# print(list) 
# list.append(4)
# print(list)             #mutating the list
# print(list.sort())      #prints none as it makes changes in the list and doesnt return anything 
# print(list)             #appended sorted and list
# print(list.sort(reverse=True)) #descending order sorting
# print(list)  
 
# list = ["a","d","e","c","b","f"]  
# list.reverse()
# print(list) 
# list.sort()
# print(list)            #sorting of strings
# list.insert(3,"x")     #similar to append just at particular index
# print(list)  

# list=[2,1,3,1]
# list.remove(1)
# print(list)
# list.pop(1)
# print(list)

# tup = (2,1,3,1)
# print(tup[0])
# print(tup[1]) 
# #tup[0]=7         #error-tuple doesnt allow assignment similar to string
# print(tup[1: ])   #tuple slicing similar to lists

# tup={}           #empty tuple
# print(tup)       
# print(type(tup))  

# tup=(1, )        #single element tuple - remember to use comma else considered as integer 
# print(tup)        
# print(type(tup)) 

#tuple methods
# tup=(2,1,3,1)
# print(tup.index(1))
# print(tup.count(2))

#wap to ask the user to enter their 3 favourite movie and store them in a list
# movies=[]
# mov1=input("Enter 1st movie: ")
# mov2=input("Enter 2nd movie: ")
# mov3=input("Enter 3rd movie: ") 

# movies.append(mov1)
# movies.append(mov2)
# movies.append(mov3) 

# print(movies) 
# or
# movies=[]
# movies.append(input("Enter 1st movie: "))
# movies.append(input("Enter 2nd movie: "))
# movies.append(input("Enter 3rd movie: ")) 
# print(movies) 

#wap to check if a list contains a palindrome of elements
# list1=[1,2,8]  #same can be done for list1=["m","a","a","m"]

# copy_list1=list1.copy()
# copy_list1.reverse()

# if(copy_list1==list1):
#     print("List is Palindrome")
# else:
#     print("Not Palindrome")

#wap to count the number of students with the grade A in the following tuple
# grade=("c","d","a","a","b","b","a")
# print(grade.count("a")) 

# #store the above values in a list and sort them from a to d
# grade=["c","d","a","a","b","b","a"]
# grade.sort()
# print(grade) 
