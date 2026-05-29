                    #ASSIGNMENT 1 👇👇

# problem 1:- write a python program to declare variables or different data such as...
#a) integer b)float c)string d)boolean 👉👉

#a)integer
num=1234
print(num)
print("Data type is:-",type(num))

#b)float
a=12.45
print(a)
print(" Data type is:-",type(a))

#c)string
str="saloni"
print(str)
print("Data Type is :-",type(str))

#d)boolean
a= True
b= False

print(a)
print("Data Type is :-",type(a))

print(b)
print("Data Type is :-",type(b))


#Problem 2 create a string variable with your name and perform the following operations 👉👉

# a)Convert it into uppercase
name="saloni agarwal"
upper_case= name.upper()
print("upper case:-",upper_case)

# b)Convert it into lowercase
branch="CSE"
lower_case= branch.lower()
print("lower case:-",lower_case)

#c) find the length of the string
str="upflairs"
print("length of my string is:-",len(str))

#d) replace one character with another
str="computes"
print("replace correct str:-",str.replace("s","r"))


#Problem 3:- write a python program to check whether a given word is a palindrone or not using string slicing 👉👉

str="wow"
print( str[: :-1])


#Problem 4:- create a list of 10 numbers and perform the following operations

#a) Add a new element 
lst=[1,2,3,4,5,6,7,8,9,10]
lst.append(11) # adding element
print(lst)

#b) remove an element 
lst=[1,2,3,4,5,6,7,8,9,10]
lst.remove(10) # deleting element
print(lst)

#c) sort the list
lst=[2,5,9,1]
lst.sort()
print(lst)

#d) find the maximum and minimum value
lst=[2,5,9,1]
print(max(lst))   #maximum value
print(min(lst))   #minimum value

#Problem 5:- write a python program to count how many even and odd numbers are present in a list 

a=[1,2,3,4,5,6]
even=0
odd=0
for num in a:
    if num%2==0:
        even+=1
    else:
        odd+=1
print("even number:-",even)
print("odd number:-",odd)    


#Problem 6:- create a tuple containing 5 subjects. print:👉👉

#a) First element
tpl=("python","web","hello","hii","ai")
print(" my first element is:-",tpl[0])

#b)last element
print(" my last element is:-",tpl[-1])

#c) length of the tuple
print("length of my tupple is:-",len(tpl))

#d) check whether a subject exists in this tuple or not
tpl=("python","web","hello","hii","ai")
print("hello" in tpl)

#Question 7:- write a python program to crete a dictionary of student details containing👉👉

#a)name b)age c) course d) marks

dict={"name":"saloni",
      "age":20,
      "course":"data science",
      "marks":79}
print(dict)
print("the keys is:-",dict.keys())
print("the values is:-",dict.values())


#Problem 8:- write a python programs to update and delete elements from a dictionary👉👉

dict={"name":"saloni","branch":"cse","age":20,"sub":"python"}

dict['sub']="data science"   ##updating an element
print(dict)

dict.pop('age')              ##deleting an element
print(dict)


#Problem 9:- create two sets and perform the following set operations👉👉

#a) union
s1={1,2,3,4}
s2={3,4,5,6}
print (s1.union(s2))

#b) intersection
s1={1,2,3,4}
s2={3,4,5,6}
print(s1.intersection(s2))

#c) difference
s1={1,2,3,4}
s2={3,4,5,6}
print(s1-s2)

#c)  symmetric difference
s1={1,2,3,4}
s2={3,4,5,6}
print(s1^s2)


#Problem 10:- write a python program to remove duplicate values from a list using a set 👉👉

lst=[1,2,3,4,5,6,2,3,5]
#convert list to set because in list we dont have duplicates values
new_lst=list(set(lst))
print("original list:-",lst)
print("list after removing duplicate values:-",new_lst)
