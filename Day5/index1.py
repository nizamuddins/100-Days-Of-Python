# for loop

stuheight = input('Enter students heights?').split(' ');

sum = 0;

for num in stuheight:
    sum += int(num);


print(sum)

students = 0; 

for num in stuheight:
    students += 1;

print(students);

height = round(sum/students);
print(height)


