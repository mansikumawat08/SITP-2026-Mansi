print("hello")
print("123hello")


x="1"
y="Mansi"
print(type(x))
print(type(y))


x=y=z ="orange"
print(x)
print(y)
print(z)


a="ABC"
x="A"
y="B"
z="C"

print(x)
print(y)
print(z)


print ("hello",end=" ")
print ("world")

# VARIBLE -- variables are containers for storing data values
#a variable must start with a letter or underscore
# A variable name cannot start with number
# A variable name can oly contain alpha-numeric characters and underscores
# variable names are case sensitive (age, Age, AGE are 3 different variables)
## this means uppercase and lowercase vaiables are treated as different variables
# variable name cannot be of any python keyword

myvar ="john"
my_var= "john"
_my_var ="john"
myVar = "john"
MYVAR ="john"
myvar2 ="john"

print(34)
print("salman khan")
print ("divya",23,78.9,True)
print("divy",23,"radhika")

print("hello kaha se ho aap", end=" ")
print("main jaipur se hu")

print("hello", end="-")
print("world")

print("hello");print("how are you");print("i'm okay")

#dynamic typing --- c,c++ language you have to tell the datatype befrore giving value to 

print(x)
print(type(x))
#dynamic binding == in python there is no fix datatype 

a = 47
print(a)

a = "Mansi"
print(a)

a = int('4') #str->int
print(a)
print(type(a))   #casting

#many values to many variables --python allows you to assign values to multiple variables

x,y,z= "apple","cherry","orange"
print(x)
print(y)
print(z)

#unpack c a collection-- if you have a collection of values in a list, tuple etc.
#python allows you to extract the values into variables. this is called unpacking

#list
a= ["Mansi","Apple","juice"]
x,y,z=a
print(x)
print(y)
print(z)

# tuple unpacking
x=(7,8,9)
a,b,c=x
print(a,b,c)

# string unpacking
name="ABC" 
a,b,c = name
print(a,b,c)

x= "python" 
y="is"
z="good"
print(x,y,z)


##casting--if you want to specify the datatype of a variable, this can be done with casting
x= int(3)
y=float(3)
z=str(3)
print(x)
print(y)
print(z)
print(type(z))

## type conversion --- you can convert one data type into another with the int(), float()
#1. implicit type conversion -- internally know the datatype

print(7+8.8)
print(type(7),type(8.8))

#2. explicit type conversion -- programmer request to change the data type

x= float(20)
print(x)

# user input
# static vs dynamic software
#1. static-- don't talk with user they only give information(eg--calender, blog,watch )
#2. dynamic -- user input deta h (eg-- youtube, ola, zomato)

# a =input("what is your name: ")
# b =input("what is your age")
# print(a)
# print(b)

# a =int(input("enter first number:"))
# b =int(input("enter second number:"))

# c=a+b
# print(c)


# name= input("apna naam bato: ")
# print("hello",name)

# a= int (input("enter a number: "))
# b= int (input("enter second number: "))

# sum = a*b
# print("total: ",sum)


#swap 2 numbers program



# a=20
# b=12

# a,b =b,a
# print("A:",a)
# print("B: ",b)



# a=20
# b=12
# c=30

# a,b,c=c,a,b
# print("A:",a)
# print("B:",b)
# print("C:",c)


#string rules - 
#1 sequence of characters written inside quotes.
#2 includes letters, numbers ad spaces
#3 strings are immutable
#4 but we can manipulate strings- using methods like concatenation, slicing, formatting to create a new string
#.. delete an entire string variable (in python it is not possible to delete indivisual character from string)

# a = 'hello'
# print(a)

# b = "python is good"
# print (b)

# c = '''hey how are you
# sab badiya
# main theek hu'''
# print(c)

#day(3)
#Antigravity (like vs c)(time and space coplexity less)
print("hello hi")

#python has 0 datatypes
# all the datatypes that we use are builtin (already defined )
#(str, float, boolean , int , float,set , complex, list , tuple)
#str
# name = "Diya"
# print("My name is :- ",name)

# print("type of my variable is:- ",type(name))## type function is used to check the type 

# print("len of my string is:- ",len(name))## len to check the length of the string
# upper_case = name.upper()# used to convert inyo uppercase
# print("upper case :- ",upper_case)
# lower_case =upper_case.lower()# used to convert into lowercase
# print("lower case:- ",lower_case)

# lw =upper_case.casefold()# converts into lowercase## task 1
# print(lw)

# name ="dev"
# print(name.title())# converts first letter into capital letter
# print(name.capitalize())# also converts first letter into capital##task 2

# company_name = "upflairs    "# space ko b count krta h 
# print(len(company_name))
# print(company_name.strip())

# #intro="hello hii kese ho"### task 3

# #indexing and slicing
# # len = position
# company_name = "upflairs"
# print(company_name[0])
# print(company_name[7])
# print(company_name[-1])# for last character

# print(company_name[0:3])# characters using indexing range
# # company_name >>>>task 4 reverse the string

# name = "ritik"
# last_name = "kumar"
# print(name +" "+last_name)# join

# str*str
name = "Dev"
#print(name * name)# error 
#print(name + name)
#print(name + 2)
# print(name * 2)# prints name 2 times

# intro=""" hi..... mansjiiijnncnuidchiicndcnaoiejfcdm,ca.,jijcioefgeculsdkdslakdidueyfc"""# more than 1 or  2 line use triple quotes
# print(intro)

#name ='dev'
#name = "dev"### difference btw both

#split
#intro = "hello my name is \n Mansi"
#intro.split("\n"," ")

# name = "Govind"
# address = "Jaipur"
# print(f"my name is {name} and i am from{address}")

# #input function(user se input lene k liye)
# name = (input("enter your name:-"))
# print(name)
# print(type(name))

#typecasting using int before input as done above

# LIST
# muteable
# hetreogeneous
# allows duplicate values
lst = [1,2,3,2,3,"hello",2.3]
print("This is my first list:- ",lst)
print ("len of my list is:- ",len(lst))
print("type of my list is:- ",type(lst))

# print = 10
# print(print)# error

# list = 10 
# print(">>>>><><<<<",list)

# indexing
lst =[1,2,3,4,7,8,9,"hello",3.4]
print(lst[0])
print(lst[1])
print(lst[3])

print(lst[-1])# negative indexing

print(lst[0:4])
print(lst[2:4])
      
fruits = ["apple", "cherry","grapes"]
#add item
fruits.append("orange")# append adds the element at last position
print("fruits list :- ",fruits)

fruits.insert(0,"banana")# inserts element at a specific position 0 denotes index and banana is item
print("fruits list:- ", fruits)

fruits.remove("apple")
print("fruits list:- ",fruits)# removes the item

fruits.pop(1)
print("fruits list:- ",fruits)# removes element of a particular index

#fruits.clear()
#fruits.copy()
#print(fruits.count("apple"))
print(fruits.index("banana"))

fruits[0] = "kiwi"

fruits.reverse()
print("reverse list is :-",fruits)

lst1 = [1,2,3]
lst2 = [7,8,9]
print(">>>>>>>>>",2 in lst1)
print(lst1 + lst2)# concatenation


# len()length of list
# max()maximum value in the list
# min()min value in the list
# sum() sum of all values in the list
#sorted() sorted version of list
#codeshare.io/G7QXkb

# Tuple
tpl =(1,2,34,"hello",2.3,1,2)
print("this is my first tuple",tpl)
print("len of my tuple:- ",len(tpl))
print(tpl[0])
print(tpl[1])
print(tpl[3])

print(tpl[0:3])
print(tpl[2:4])
print(tpl[0 : 3 : 7])

#bydefault elements tuple m mane jate h
a = 1,2,3,"hello",2.3
print(a)
print(len(a))
print(type(a))

#tuple unpacking
a,b,c = 1,2,3
print(a)
print(b)
print(c)
# error case
# a,b,c =1,2
# print (a)
# print (b)
#no. of var. should match no. of elements

tpl = (1,2,3,"hello",3.3,3) 
print(tpl)
print (tpl.count(3))# counts no . of time a value occured
print (tpl.index(2))# shows index of a particular element

#typecasting for adding elements(as tuple is immutable)
tpl = (1,2,3,"hiii",7,8)
print ("this is my tuple: - ",(tpl))
print(type(tpl))
print ("converting tuple into list")
lst = list(tpl)
print (">>>>>",lst)
print (">>>>>>",type(lst))
lst.append(100)
print(lst)
tpl = tuple(lst)
print(tuple)
# in this we have converted the tuple into list a tuple
# nd then using append function we added the element needed and again converted it into 

# dictonary
#collection of key and value
#key should be unique but we can have duplicate values
# its muteable
# key + value = item

student = {"name":"Mansi",
           "class":"second yr",
           "roll no.":"18",
           "branch":"IT",
           "address":"ajmer"}
#name, class , roll no. ,branch , address >>>>> keys
#Mansi, second yr ,18, IT, ajmer >>>> values
print(student)
print("dictonary keys:- ",student.keys())
print("value indictonary are:- ",student.values())
print("items in diconary are:- ",student.items())

#here we can get values with keys
print(student["name"])
print(student["class"])

#add item in python dict
student["subject"]="python"
print (student)

#update : used to update the values f key # tsk1 
# fromkeys #tsk2

# print(student.get("name"))# get.() also gives value for particular key

# student1 = {"name":"Mansi",
#            "class":"second yr",
#            "roll no.":"18",
#            "branch":"IT",
#            "address":"ajmer"}

# print(student1.pop("roll no."))# removes particular item
# print(student1.copy())

# print(student1.popitem())

car = {
    "brand":"Ford",
    "model":"Mustang",
    "year":1984
    }

x= car.setdefault("colour","white")
print(x)
print(car)

# deepcopy #tsk2

car = {
    "brand":["Ford","Honda","hero"],
    "model":"Mustang",
    "year":1984
    }

print(car)

car["year"]=2000
print(car)# updating value of a key without using update function

# python has only 2 tyoes of loops :- for and while
# iteration = for loop

for x in car:
    print(x)
# if the output is in form of row <<<<< iterartion
# bydefault it is for key

for x in car.values():# for values
    print(x)

for x in car.items():# for items
    print(x)

# set
#muteable
#fastest
#unordered 
#no duplicate values allowed
# no slicing 
#no indexing
set1 = {1,2,3,4}
print("this is my first set:-",set1)
print("type of set:- ",type(set1))
print("len of my set:- ",len(set1))

# remove m if element is not present it will show error
# but in case of discard it will print the same set without any error 

set1.remove(1)
print(set1)
set1.discard(2)
print(set1)

#set1.remove("hello")# will show error
set1.discard("hello")


##Assignment 4

##In python ,data types defines the type of value a variable can store
#### Variables can store data of different types, and different types can do different things.


#1 INTEGER: An integer is a whole number without a decimal point.
# It can be positive, negative, or zero. 
# Syntax : variable_name = integer_value
##example:
a = 10
b = -25
c = 0

print(a)
print(type(a))

####Features
# No decimal point
# Supports arithmetic operations
# Unlimited length in Python

# 2. Float (float)

# A float is a number with a decimal point.

# Syntax :variable_name = float_value

# Features
# Stores decimal values
# Used in scientific calculations
# More precise than integers for fractional values

pi = 3.14
temperature = -12.5

print(pi)
print(type(pi))
####3String (str)
# A string is a sequence of characters enclosed in quotes.
# Syntax :variable_name = "text"

# Features
# Used to store text
# Immutable (cannot be changed directly)
# Supports indexing and slicing

name = "Mansi"
city = 'Jaipur'
print(name)
print(type(name))
text = "Python"
print(text[0])      # First character
print(text.upper()) # Convert to uppercase

#####4. Boolean (bool)
# A Boolean data type stores only two values:
# True
# False
# Syntax :variable_name = True
# eatures
# Used in conditions and decision making
# Important for if, while, and logical operations
is_passed = True
is_raining = False

print(is_passed)
print(type(is_passed))


####5. List (list)

# A list is an ordered and mutable collection of items.
# Syntax:list_name = [item1, item2, item3]
# Features
# Ordered
# Mutable (can be changed)
# Allows duplicate values
fruits = ["apple", "banana", "mango"]
print(fruits)
print(type(fruits))
# Operations on List
numbers = [1, 2, 3]
numbers.append(4)
print(numbers)
numbers.remove(2)
print(numbers)


# 6. Tuple (tuple)
# A tuple is an ordered but immutable collection of items.
# Syntax :tuple_name = (item1, item2, item3)
# Features
# Ordered
# Immutable (cannot be modified)
# Faster than lists
# Allows duplicate values
# Example
colors = ("red", "green", "blue")

print(colors)
print(type(colors))

# 7. Set (set)
# A set is an unordered collection of unique items.
# Syntax :set_name = {item1, item2, item3}
# Features
# Unordered
# No duplicate values allowed
# Mutable
# Example
numbers = {1, 2, 3, 4}
print(numbers)
print(type(numbers))
# Set Operations
a = {1, 2, 3}
b = {3, 4, 5}
print(a.union(b))
print(a.intersection(b))

# 8. Dictionary (dict)
# A dictionary stores data in key-value pairs.
# Syntax :dict_name = {
#     key1: value1,
#     key2: value2}
# Features
# Stores data in key-value form
# Mutable
# Keys must be unique
# Example
student = {"name": "Mansi","age": 20,"course": "IT"}
print(student)
print(type(student))
#  Adding New Data
student["city"] = "Jaipur"
print(student)

# QUESTION2

# Python Program to Demonstrate Dynamic Typing and type() Function

# Integer
a = 10

# Float
b = 3.14

# String
c = "Mansi"

# Boolean
d = True

# List
e = [1, 2, 3, 4]

# Tuple
f = (10, 20, 30)

# Set
g = {1, 2, 3}

# Dictionary
h = {"name": "Mansi", "course": "IT"}

# Printing values and their data types
print("Value of a:", a)
print("Data Type of a:", type(a))

print("\nValue of b:", b)
print("Data Type of b:", type(b))

print("\nValue of c:", c)
print("Data Type of c:", type(c))

print("\nValue of d:", d)
print("Data Type of d:", type(d))

print("\nValue of e:", e)
print("Data Type of e:", type(e))

print("\nValue of f:", f)
print("Data Type of f:", type(f))

print("\nValue of g:", g)
print("Data Type of g:", type(g))

print("\nValue of h:", h)
print("Data Type of h:", type(h))
# Demonstrating Dynamic Typing
x = 100
print("\nValue of x:", x)
print("Data Type of x:", type(x))

x = "Python Programming"
print("\nNow Value of x:", x)
print("Now Data Type of x:", type(x))

# 3
# mutable data type
# list is mutable data type
lst=[10,20,30]
print(lst)

#string are immutable
name = "Python"

# name[0] = "J"   ❌ Error

new_name = "J" + name[1:]

print(new_name)

#4
#list operations
lst=[1,2,3,4,5]
print(lst)
lst.append(6)
print(lst)
lst.remove(2)
print(lst[0:4])

# #tuple indexing
tup=(10,20,30,40,50)
print(tup[0])
print(tup[1])
print(tup[2])
print(tup[3])
print(tup[4])

# #set operations
sat={1,2,3,4,5}
print(sat)
sat.union({6,7})
print(sat)
sat.intersection({2,3,4})
print(sat)

# #dictionary keys
student={"name":"Aman","age":20,"course":"Data Science"}
print(student["name"])
print(student["age"])
print(student["course"])
student.keys()
print(student.keys())
student.values()
print(student.values())
student.items()
print(student.items())
#5
#min student management system
student={
    "name": "Mansi",
    "roll_no": 18,
    "course": "B.Tech IT"
}
#store marks using list
student["marks"] = [90, 93, 87]
#calculate average marks
total=sum(student["marks"])
#calculate average
average=total/len(student["marks"])
print("Student Name:", student["name"])
print("Roll No:", student["roll_no"])
print("Course:", student["course"])
print("Marks:", student["marks"])
print("Average Marks:", average)
