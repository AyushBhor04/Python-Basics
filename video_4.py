#Dictionary
# info={
#     "key":"value",    #key value can be anything immutable , mostly strings
#     "name":"Ayush",
#     "learning":"coding",
#     "age":23,
#     "is_adult": True,
#     "marks": 98
# }
# print(info) 


# info={
#     "name":"ApnaCollege",          
#     "subjects":["python","c","Java"],
#     "topics":("dict","set"),
#     "age":23,
# }
# print(info) 
# print(type(info)) 

#accessing in dictionary
# info={
#     "name":"ApnaCollege",          
#     "subjects":["python","c","Java"],
#     "topics":("dict","set"),
#     "age":23,
#     "is_adult": True,
#     12.99 : 94.2 
# }

# print(info["name"])
# print(info["topics"])
# print(info["subjects"])
# print(info["age"]) 
# # print(info["surname"]) #error

# info["name"]="Ayush"    #overwrites the old value
# info["surname"]="Bhor" 
# print(info)  

#Null Dictionary
# null_dict={}
# print(null_dict) 
# null_dict["name"]="Apna_College"
# print(null_dict) 

#Nested Dictionary
# student={
#     "name":"Ayush",
#     "subjects" : {
#         "phy":97,
#         "chem":98,
#         "math":92
#     }
# }
# print(student)
# print(student["subjects"])
# print(student["subjects"]["chem"]) 

#Dictionary Methods
# student={
#     "name":"Ayush",
#     "subjects" : {
#         "phy":97,
#         "chem":98,
#         "math":92
#     }
# }
# print(student.keys()) #nested doesnt come as output
# print(list(student.keys())) #type_casting
# print(len(student))
# print(student.keys())
# print(len(list(student.keys()))) #type_casting
# print(student.values())
# print(list(student.values())) 
# print(student.items()) 
# print(list(student.items())) 

# accessisng 
# pairs =list(student.items())
# print(pairs[0]) 

# print(student["name"])
# print(student.get("name"))        #both gives same name

# print(student["name2"])      #error
# print(student.get("name2"))  #null and not error

# student.update({"city":"Mumbai"})
# print(student) 

# new_dict={"name":"Bhor","age":16} 
# student.update(new_dict) 
# print(student)    
# print(new_dict) 

#Sets
# collection = {1,2,2,2,3,4,"hello","world","world",5}  #ignores repeated values and is unordered
# print(collection)
# print(type(collection))
# print(len(collection))                                #ignores duplicate values again 

# collection={} #empty dictionary 
#  #empty set
# print(type(collection)) 

#Set methods
# collection=set()
# collection.add(1)
# collection.add(2)
# collection.add("Apna college")
# collection.add((1,2,3))      #tuple
# collection.add([1,2,3])      #error in saving list 
# collection.remove()
# print(collection)
# collection.remove(5) #error
# print(collection)
# collection.clear()  
# print(len(collection))

# collection={"hello","world","Apna college","Coding","Python"}
# print(collection.pop())         #pops random
# print(collection.pop())         

# set1={1,2,3}
# set2={2,3,4}

# print(set1.intersection(set2))  #produce new set 
# print(set1.union(set2))
# print(set1)
# print(set2) 

#store following word meaning in a python dictionary
# dictionary = {
#     "cat" : "a small animal" ,
#     "table" : ["a piece of furniture","list of facts and figures"]
# }
# print(dictionary) 

#given a list of subjects for students , assume one classroom 
# is recquired for 1 subject . 
#how many classrooom are needed by all students 
# subjects={
#     "python","java","c++","python","java script",
#     "c","C++"
# }
# print(len(subjects)) 

#wap to enter marks of 3 subjects from the user and store them in a dictionary
#start with an empty and add one by one 
#use subject name as key and marks as value

# marks={}
# x= input(("enter phy : "))
# marks.update({"phy": x}) 

# x= input(("enter math : "))
# marks.update({"math": x}) 

# x= input(("enter chem : "))
# marks.update({"chem": x}) 

# print(marks) 

#figure out a way to store 9 and 9.0 as a seperate values in set
#(you can make use of builtin data types)
# values={9,9.0}
# print(values)        #treats as same values
# values = {9,"9.0"}
# print(values)          #treats as different values 
# values={
#     ("float",9.0),
#     ("int",9)
# }
# print(values) 