marks = input('Enter students marks?').split(' ');
num = 0;
for m in marks:
    for n in marks:
        if m > n:
            num = m;
        else:
             num = n;

print(num);
