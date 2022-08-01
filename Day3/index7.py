print('Welcome to Pytgon pizza Deliveries');

size = input("what size pizza do you want?S, M or L");

bill = 0;

if size == "S":
    add_pep = input("Do you want pep? Y or N");
    x_cheez = input("Do you want xtra cheez? Y or N");

    bill += 15
    if add_pep == "Y":
        bill += 2;
        if x_cheez == "N":
         print(f'total bill is ${bill}');
        else:
           bill += 1;
        print(f'total bill is ${bill}');
    else:
        if x_cheez == "N":
            print(f'total bill is ${bill}');
        else:
                bill += 1;
                print(f'total bill is ${bill}');
           
elif size == "M" :
    bill += 20
    add_pep = input("Do you want pep? Y or N");
    x_cheez = input("Do you want xtra cheez? Y or N");

    if add_pep == "Y":
        bill += 3;
        if x_cheez == "N":
         print(f'total bill is ${bill}');
        else:
           bill += 1;
        print(f'total bill is ${bill}');
    else:
        if x_cheez == "N":
            print(f'total bill is ${bill}');
        else:
                bill += 1;
                print(f'total bill is ${bill}');
elif size == "L":
    bill += 25
    add_pep = input("Do you want pep? Y or N");
    x_cheez = input("Do you want xtra cheez? Y or N");

    if add_pep == "Y":
        bill += 3;
        if x_cheez == "N":
         print(f'total bill is ${bill}');
        else:
           bill += 1;
        print(f'total bill is ${bill}');
    else:
        if x_cheez == "N":
            print(f'total bill is ${bill}');
        else:
                bill += 1;
                print(f'total bill is ${bill}');    
else:
    print("Please select the correct size")