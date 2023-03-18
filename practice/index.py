# version:python3

# python: python is a high level and Object-Oriented Programming Language;

# Why python:
# .Easy to use
# .Expressive Language

# Applications:
# 1)Web deevelopment
# 2)software deevelopment
# 3)Mathematics

# .Its syntax is simple similar to english
# .python uses new line for each command
# .It relies on indentation,using white space for definig functions,loops and classes


# Varibles: 
# variables are the names to which values are assign and use them as a referenced throughout the program
# variables keeps value accessible
# variables gives context to values
# values are assigned to variables using assignment Operator "="

# points to be followed while defining Varibles
# .variables names can contains numbers,letters and underscores
# .variables can't contains spaces
# .variables cannot star with numbers
# .variables are case-sensitive

# name = "Nizam";
# a1 = 2;
# _a = 23;
# user_name ="itsnizam";

# I/O Operations

# print:print function prints the message as output on the screen

# print("I amm Back"+" From Sleep");
# print('Md nizam'+' From  Hyderabad');

# end parameter
# print("nizam",end="");
# sep parameter
# print("Nizam","Uddin",sep="@")

# input:It takes input from user

# name = input("Enter your name");
# print(name);

# Different types of datatypes=>

# Text Type:str
# Numeric Types:int, float, complex
# Sequence Types:list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# None Type:	NoneType

# name = "nizam";=>string
# num = 2;=>int
# f = 2.5=>float
# list1 = [1,2,4,5,67];=>list
# tuple1 = (1,3,5,7);=>tuple
# dict2 = {
#     "name":"nizam",
#     "age":21
# }=>dict
# set1 = {4,6,87,6,6,9};=>dict
# print(set1)
# n1 =23;
# n2 =23;
# print(n1 == n2)=>Boolean

# Operators=>
# Operators are used to perform Operations on variables

# arthematic Operators=>
# +,-,*,/,%,**
# assignment Operators=>
# =,+=,*=,-=,/=
# Comparison Operators=>
# ==,>,<,>=,<=,!=
# logical Operators=>
# and,or,not
# Identity Operators=>
# is,is not
# MemberShip Operators=>
# in,not in
# Bitwise Operators=>
# &,|,~,<<,>>

# conditional statements=>
# It is used for decision making ,By checking a conditions,if condition is satisfied then we execute a block of code or if the condition is false we execute a block of code

# types of conditional statements=>
# if/else
# nested if/else
# if/elif

# type checking by type() and isinstance(variable,datatype)=>

# val = 23;
# print(type(val));

# string = "Nizam";
# print(type(string));

# bol = True;
# print(type(bol));

# float2 = 2.5;
# print(type(float2));

# s ="nizam"
# print(isinstance(s,str))
# print(isinstance(s,int))

# ============================================
# str,int,float,

# val = str(45);
# val = str(45.67);
# print(type(val));
# char = float("nizam")x
# char = int("nizam")x

# f string=>

# val = 23;
# print(f"the value is {val}");
# function

# len()=>
# string = 'Nizam';
# print(len(string))

# loops=>

# string = "Nizam";

# for i in string:
#     print(i)

# for i in range(0,len(string),2):
#     print(i)

# i=0;
# while i<len(string):
#     print(string[i]);
#     i+=1;


# =============================================
# list

# li = [2,4,67,6,7,8];

# print(len(li))
# print(type(li))
# li[0] = 10;
# print(li[0]);
# for i in range(0,len(li)):
    # print(li[i])

# for i in li:
#     print(i)

# for i,x in enumerate(li):
#     print(i,x)

# Operations on List

# li = [2,4,67,2,6,7,8];
# pop
# print(li.pop())
# print(li)

# remove
# li.remove(2);
# print(li)
# li.pop(0);
# print(li)

# append
# li.append(8);
# print(li);
# insert
# li.insert(len(li),9)
# print(li);

# li.extend([5,6,8,9]);
# print(li);

# l2 = li.copy();
# print(l2)

# spread operator=>
# one way
# l = [2,4,5];
# b = [*l];
# l[0]=1;
# print(b)

# second way
# l = [2,4,5];
# b = [];
# b.extend(l);
# print(b)
# =======================================


# other functions

# string = "mdnizam";
# print(string.upper())
# print(string.lower())

# print(min(5,7,4));
# print(min(li));
# print(max(li));
# print(li.count(2));
# li.reverse()
# print(li)
# li.sort();
# print(li);
# li.clear();
# print(li);

# split() functions=>

# string = "Md'Nizam'Uddin";
# s = string.split("'");
# print(s)

# string = "MdNizam";
# s = [char for char in string];
# print(s)

# reverse()=>Does not return
# s.reverse()
# print(s)

# join()=>returns
# s2="".join(s) 
# print(s2)

# sum()=>
# It takes Just iterables

# print(sum(li));

# ==================================================

# random and math
# import random
# import math

# re = random.randint(0,10);
# print(re)

# re1 = math.floor(random.random()*3)+1;
# print(re1)

# [ math.round() - rounds to the nearest integer (if the fraction is 0.5 or greater - rounds up)
# math.floor() - rounds down
# math.ceil() - rounds up ]

# li = [2,5,7,9];
# random.shuffle(li);
# print(li)

# ch = random.choice(li);
# print(ch)

# ================================================================

# functions=>
# A function is a Sequence of instructions which performs a particular task and it takes input as a parameter and output a value after performing a specific Operations

# why do we need functions
# it is reusable
# it maintains a neat code
# It provides modularizations
# Easy Debugging

# keywords=>

# break
# Used to terminate loops

# continue
# Used to ignore a element and continue

# return
# Used in functions to return value as output

# def func(a,b):
    # return a+b

# print(func(6,7))

# default functions=>
# def func(a,b=3):
#     return (a+b);

# print(func(4,1));

# rest functions=>
# def func(a,b,*c):
#     print(a,b,c);

# func(3,5,6,78,7)

# ===========================================================

# Strings

# A string is a datatype in python which stores the characters as a string and it is immutable

# Creation of string

# string = '''
# I am Nizam,
# I from Hyderabad
# '''
# print(string);

# s1 = 'Iam nizamn';
# print(s1);

# s2 = "I am Nizam";
# print(s2);

# # To print sentence in Different lines
# s3 = "Iam Md nizam\nfrom Hyderabad";
# print(s3)

# # Concatenation of string

# s5 = "md nizam"+" from hydeabad"
# print(s5);

# # accesing characters through indexing
# s = 'Iam mdnizam';
# print(s[-1]);
# print(s[0])

# ======================================================
# dictionaries=>
# Dictionaries are used to store a data in key value pairs;and its i mutuble and it does not allow duplicates

# syntax
# dic1 = {
    # "key":"value"
# }

# example=>

# dic1 = {
#     "Name":"Nizam",
#     "Age":22,
#     "occupation":"Student"
# }
# dict2 = {}
# Accesting value of particular key=>

# print(dic1["Name"]);
# print(dic1["Age"]);

# # changing value=>
# dic1["Name"] = "Nomaan"
# print(dic1["Name"]);
# dict2["Name"] = "Nayeem";
# print(dict2);
# print(type(dict2))

# length of dictionaries
# print(len(dic1));
# print(len(dict2))

# Adding key value
# dic1["Address"] = "Hyderabad";
# print(dic1);

# iterating Dictionaries

# for i in dic1:
#     print(f'{i}:{dic1[i]}')


# Dictionaries can alse be created using dict() keyword
thisdic = dict(Name="Mahmood",clas="10th");
# print(type(thisdic));
# print(thisdic)
# print(thisdic["Name"])

# for i in thisdic:
#     print(f'{i}:{thisdic[i]}')

# To get keys in the form of list
# syntax=>

# dictionarieName.keys();
# example=>
# print(thisdic.keys())

# for i,x in enumerate(thisdic):
#     print(i,x)

# delete keyvalue in dictionaries
# del thisdic["Name"]
# print(thisdic)
# =====================================================================

# Tuples=>
# It stores elements of Different datatypes and unlike list it is immutable
# It can also access through indexing and it allows duplicates

# syntax=>
t = ("Name","age","class");
# print(type(t))
# print(len(t));
# print(t[1])

# delete element in Tuples=>
# You cant delete a elements in Tuples but you can delete a tuple completely

# print(t)
# del t
# print(t)

# iterating=>

# for i in t:
#     print(i)

# tuple() constructor=>
# thistuple = tuple(("name","age"));
# print(type(thistuple))

# single element tuple=>
# thistuple = ("nizam") X
# print(type(thistuple))

# thistuple = ("mdnizam",);
# print(type(thistuple))


# ==================================================================================
# Set=>
# It stores elements of Different datatypes and it is immutable and cnnot access through indexing

# syntax=>
# set1 = {"nizam","2",2,1}
# print(type(set1))
# print(len(set1))
# for i in set1:
#     print(i);
# print(set1)    

# delete element in set=>
# set1.remove("nizam") => raise a exception if element does not exits
# set1.discard("2") => does not raises exception if element does not exits
# print(set1)

# # set() constructor=>
# thisset = set(("name","age"));
# print(type(thisset))

# class=>
# classes is a blueprint of objects or it is used to create instances of objects

# static method=>
# class objects:
#     def sum(a,b):
#         return a+b;

# re = objects;
# print(re.sum(2,4));

# creating a objects and Methods
# class Myfunc:
#     def __init__(self,val):
#         self.val = val;
#         self.next = None;
#     def Myfunc2(self):
#         return(self.val)

# re2 = Myfunc(1);
# print(re2.next)
# print(re2.val)     
# print(re2.Myfunc2())

# Inheritence=>
# creating a child class from parent class
# class Parent:
#     def __init__(self,val):
#         self.val = val;
#         self.next = None;
#     def Myfunc2(self):
#         return(self.val)

# class Student(Parent):
    # pass
#  we can use pass keyword to Inherit all the properties and methosds from parent class
# re2 = Student(2);
# print(re2.val);
# print(re2.Myfunc2());

# if to add properties and more methods we should Use a super() function to Inherit a all properties and methods and add more
# class Parent:
#     def __init__(self,val):
#         self.val = val;
#         self.next = None;
#     def Myfunc2(self):
#         return(self.val)

# class Student(Parent):
#     def __init__(self,val,name,age):
#         super().__init__(val)
#         self.name = name;
#         self.age = age;
#     def Myfunc3(self):
#         return(self.name)            
#  we can use pass keyword to Inherit all the properties and methosds from parent class
# re2 = Student(2,"Mdnizam",22);
# print(re2.val);
# print(re2.Myfunc2());
# print(re2.Myfunc3());

# slice

# l = "Nizam";
# l2 = *l;
# print(l2)
# s = l[0:2];
# print(s)

# l1 = [2,4,5,67];
# s1 = l1[0:1];
# print(s1)

# Making a copy of dictionaries
# l ={
#     "Name":"Nizam",
#     "Age":21
# }
# l2 = {**l};
# print(l2)

