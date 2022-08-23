import math
width = int(input("Enter a width?\n"));
height = int(input("Enter a height?\n"));

coverage = 5;

def func(w,h,c):
    num_of_cans = math.ceil((h*w)/c);
    return num_of_cans;

print(func(width,height,coverage))
