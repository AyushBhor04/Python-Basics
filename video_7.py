#File input/output
#opening and reading a file
# f=open("demo.txt","r") #C:\Users\91932\Desktop\Python_basics\demo.txt (use path if the file is not a part of the same folder)
# data = f.read()
# print(data)
# print(type(data))
# f.close() 

# f=open("demo.txt","r") 
# data = f.read(5)  #reads only 5 characters
# print(data)
# f.close() 

# f=open("demo.txt","r") 
# line1 = f.readline()  #reads line by line(line1)
# print(line1)
# line2 = f.readline()  #reads line by line(line2)
# print(line2) 
# line3 = f.readline()  #doesnt print anything or blank, since no line left to read 
# print(line3) 
# f.close() 

#writing to a file (Look over this)
# f = open("demo.txt","a")
# f.write("ill move to react js")
# f.close()

# f=open("Sample.txt","w")   #creates a new file if not already exists works for both a and w 

# f=open("demo.txt","r+")
# f.write("abc")
# print(f.read())    #points to s and starts from there
# f.close() 

# f=open("demo.txt","w+")
# print(f.read())    
# f.write("abc") 
# print(f.read())   
# f.close() 

#with syntax - no need to close the file explicitly using with as it does it by itself 
# with open("demo.txt","r") as f: 
#     data=f.read()
#     print(data) 

# with open("demo.txt","w") as f:
#     f.write("new data")

#command use to use external or uninstalled modules on our system
#pip install tenserflow    
#pip3 install tenserflow 

#deleting a file
# import os 
# os.remove("sample.txt") #deletes a file

#create a new file practice.txt using python and add
# hi everyone
# we are learning file i/o
# using java
# i like programming in java
# with open("practise.txt","w") as f:
#     f.write("hi everyone\nwe are learning file i/o\n")
#     f.write("using java\ni like programming in java")

#waf that replaces all occurences of java with python in above file
# with open("practise.txt","r") as f:
#     data=f.read()
# new_data=data.replace("java","python")
# print(new_data)  
# with open("practise.txt","w") as f:
#     f.write(new_data)

#search if the word "learning" exists in the file 
# word = "xlearning"
# with open("practise.txt","r") as f:
#     data=f.read()
#     if(data.find(word)!= -1):
#         print("Found")
#     else:
#         print("Not Found") 

#waf to find in which line of the file does the word "learning" occur first
# print -1 if not found 
# def check_for_line():
#     word = "pyqq"
#     data=True
#     line_no=1
#     with open("practise.txt","r") as f:
#         while data:
#             data=f.readline()
#             if(word in data):
#                 print(line_no)
#                 return
#             line_no+=1
#     return -1
# check_for_line() 

#from a file containing numbers seperated by comma , print the count of even numbers 
# count=0
# with open("practise.txt","r") as f: #do this well , note - splitting was used bcz it was first as a string and not integer
#     data=f.read()
   

#     num=data.split(",")  
#     for val in num:
#         if(int(val)%2==0):
#             count+=1

# print(count) 