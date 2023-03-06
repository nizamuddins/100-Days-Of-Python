# checking prime numbers
num = int(input("Enter number to check?\n"));

def prime(num1):
    flag = 0;
    for i in range(2,num1):
        if num1%i==0:
            flag = 1;
    if flag == 0 and num > 1:
        print("Prime number");
    else:
        print("Not a Prime number");
prime(num);


