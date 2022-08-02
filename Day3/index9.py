# love calculator

name1 = input("enter your name ");
name2 = input("enter her name ")

names = name1 + name2;

namess = names.lower();

t = namess.count('t');
r = namess.count('r');
u = namess.count('u');
e = namess.count('e');

true = t+r+u+e;

l = namess.count('l');
o = namess.count('o');
v = namess.count('v');
e = namess.count('e');

love = l+o+v+e;

trueLove = str(true)+str(love);

if trueLove < '10' or trueLove > '90':
    print('you are like coc and mentos');
elif trueLove > '40' and trueLove < '50':
    print('you are alrigth together' + trueLove);
else:
    print(f'your score is {trueLove}')        


