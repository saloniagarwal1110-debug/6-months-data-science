# print("hello hii kesa ho😊😊")
# name="saloni"
# print(name)
# #-name="saloni"
# #last849869name=""
# age=10
# Age=20
# AGE=30
# print(age)
# print(Age)
# print(AGE)

# #>>>>>>>>>>>>.string datatypes in python
# name="upflairs"
# print("this is my first string:-",name)
# print("type of my first string:-",type(name)) ## type func is used to tell datatype
# print("len of my first string",len(name)) # len is used to find length of my string

# num="2345"
# print(num)
# print("type of my first string:-",type(num)) ## type func is used to tell datatype

# # indexing and slicing
# # name="upflairs"
# # print(name[0])
# # print(name[3])
# # print(name[5])
# # print(name[6])

# # print("slicing:-",name[0:4])

# # print(name[-1])
# # print(name[: : -1])  #task1 


# company_name="upflairs pvt ldt"
# #lowercase convert into uppercase
# upper_case=company_name.upper()
# print("upper case😊😊",upper_case)

# company_name="upflairs pvt ldt"
# #uppercase convert into lowercase
# lower_case=company_name.lower()
# print("lower case😊😊",lower_case)


# lower_case=company_name.casefold()  ##task2
# print(lower_case)

# company_name="upflairs pvt ldt"
# first_letter=company_name.title()  #string ka  har 1st word ko capital karega
# print(first_letter)

# first_letter=company_name.capitalize()  # string ka only first letter ka 1st word ko capital karega
# print("",first_letter)


# name="saloni"
# c=name.count('a')
# print(c)
# print(name.index('l'))

# name="saloni"
# last_name="agarwal"
# print(name +last_name )
# print("😁😁",name,last_name)
# print("😁😁",name + " " +last_name)

# name="saloni "
# print(name*5)

# ## a string cannot perform mathematical operations like multiply and divide 
#     #but can multiply by no for replication of that string



# intro="""Hi, I’m Saloni Agarwal — passionate, curious, and always ready to explore new opportunities."""
# print(intro)


# name="saloni"
# print(f"my name is {name} and i am from aburoad")

# path=r"C:\Users\salon\OneDrive\Pictures\Screenshots"  #raw function for paths
# print(path)


#>>>>..list (it is a heterogeneous stores differnet types of data)

# lst=[1,2,3,4,"hello",3.14,"❤️❤️"]
# print("this is my first list:-",lst)
# print("type of my list:-",type(lst))
# print("length of my list:-",len(lst))


# print("indexing and slicing:->>>")
# lst=[1,2,3,4,"hello",3.14,"❤️❤️"]
# print(lst[0])
# print(lst[3])
# print(lst[5])
# print(lst[6])



# print("slicing:->>>>>")

# print(lst[0:3])
# print(lst[2:4])
# print(lst[4:7])
# print(lst[0:5])


# lst=[1,2,3,4,"hello",3.14,"❤️❤️"]
# lst.append("upflairs")  #add the elenent at last
# print(lst)
# lst.insert(2,"upflairs") # add elenent at specific position
# print(lst)

# lst.remove(3) #removes  element at specific position
# print(lst) 

# lst.pop()  #removes last element
# print(lst)

# lst.extend([1,0])
# print(lst)

# lst.clear()
# print(lst)

# lst=[1,2,3,4,"hello",3.14,"❤️❤️",3]
# print(lst.count(3))



# lst=[2,3,4,5]
# print(min(lst))  #largest number
# print(max(lst))    #small number
# print(sum(lst))  #total addition
# print(len(lst)) #length/count

# # for update
# # 
# lst=[1,2,7,4]
# lst.sort() 
# print(lst)

# lst.reverse()
# print(lst)

# lst[0]="hello"
# print(lst)

# #>>>>>>>>>>>>tupleA tuple is an ordered collection of elements that cannot be changed once created. In mathematics, it represents a finite sequence of objects, while in programming (like Python), it is a built-in data type used to store multiple items in a single variable, written with parentheses ( ) and separated by commas.
# #key points
# #Ordered → elements maintain their position.
# #Immutable → cannot be modified after creation.
# #Allows duplicates → e.g., ("apple", "apple").
# #Indexed → access via position, e.g., my_tuple[0].


# tpl=(1,2,3,4,5,"hello",4.5,"😁😁")
# print("this is my first tuple:-",tpl)
# print("type of my first tupple:-",type(tpl))
# print("length of my first tupple:-",len(tpl))


# print(">>>>>>>>>>>>>>...indexing and slicing<<<<<<<<<<<<<<<<<")
# print(tpl[0])
# print(tpl[1])
# print(tpl[4])
# print(tpl[5])
# print(tpl[7])
# print(tpl[2:5])

# print(tpl.count(3))
# print(tpl.index(5))

# a=1,2,3,4,"hello"  # by default it will store as tuple
# print(a)
# print(type(a))
# print(len(a))


# print("<<<<<<<<<tuple unpacking python>>>>.......")
# a,b,c=(1,2,3)
# print(a)
# print(b)
# print(c)

# a,b=(1,2,3)
# print(a)
# print(b)

# #typecasting means convert one datatype to another datatype
# tpl=(1,2,3,4,"hello")
# print("my tupple",tpl)
# print("type of my tupple",type(tpl))

# print("<<<<<<<<<<<<tuple convert into list<<<<<<<<<<")

# lst=list(tpl)
# print("this is my list",lst)
# print("type of my list:-",type(lst))

# print(".............>add item in list")
# lst.append("item add ho chuka ")
# print("list ma item add ho chuka hai:-",lst)


# print("..................>>>>>>>.list convert into tuple")
# tpl=tuple(lst)
# print("my tupple",tpl)
# print("type of my tupple",type(tpl))
# print ("tuple mai items add ho chuka hai") 


#<<<<<<<<<<<<dictionary>>>>>>>>>>>>>>>>
# dict it is keyword of dict
#pair of key and values(items)

student={ "name":"saloni",
          "class":"3rd year",
          "subject":"python",
          "rollnumber":11,
          "branch":"cse"}

#['name', 'class', 'subject', 'rollnumber', 'branch'] yah sbhi keys hai
#['saloni', '3rd year', 'python', 11, 'cse'] yah sabh values hai

# print(student)
# print(student.keys())
# print(student.values())
# print(student.items())

# print(student['name'])
# print(student['class'])
# print(student['branch'])
# print(student['rollnumber'])

# print(student.get('name'))
# print(student.get('branch'))
# print(student.get('rollnumber'))
# print(student.get('class'))

# #fromkey ,copy and deep copy ,update  ///task

print(student.pop('name'))

# car={"brand":"honda",
#         "model":2025,
#        "owner":"second owner"}

# x= car.setdefault('color','white')
# print(x)

#adding an element
# car={"brand":"honda",
#        "model":2025,
#        "owner":"second owner",
#        "car name":["Honda Amaze","Honda Elevate","Honda City","hondaCity e:HEV","Honda Civic"]}


# print(car['car name'])
# car['car name']="bmw"
# print(car)

# #update
# car['model']=2026
# print(car)


#for loop

# for x in car.keys():
#     print(x)

# for x in car.values():
#     print(x)

# for x in car.items():
#     print(x)


#<<<<<<<<<<<SET>>>>>>>>>>>>>>>>>>>>>>>>>>>.

# A set is a collection of distinct, well-defined objects (numbers, symbols, shapes, or even other sets).
# Elements of a set are written inside curly brackets { } and separated by commas.

# sat={1,2,3,5}
# print("this is my set:-",sat)
# print("len of my set:-",len(sat))
# print("type of  my set:-",type(sat))

# sat.add(10)
# print(sat)

# sat={1,2,3,5}

# sat.remove(1)
# print(sat)

# # sat.remove(10)
# # print(sat)

# sat.discard(10)
# print(sat)


#union functions
# s1={1,2,3,4}
# s2={3,4,5,6,7}

# print(s1|s2)
# result=s1.union(s2)
# print(result)

#intersection functions
# print(s1&s2)
# result=s1.intersection(s2)
# print(result)

# #difference
# print(s1-s2)

# a={1,2,3}
# b={1,2,3,4,5,6}

# print(b.issuperset(a))
# print(a.issubset(b))


# s1={1,2,3,4}
# s2={3,4,5,6}
# print(s1^s2)








