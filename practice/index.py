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

# type checking

# val = 23;
# print(type(val));

# string = "Nizam";
# print(type(string));

# bol = True;
# print(type(bol));

# float2 = 2.5;
# print(type(float2));

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

li = [2,4,67,2,6,7,8];
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

# other functions

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

# string = "Md'Nizam'Uddin";
# s = string.split("'");
# print(s)
string = "MdNizam";
s = [char for char in string];
s.reverse()
s2="".join(s) 
print(s2)











