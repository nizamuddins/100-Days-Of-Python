# Logical Operators 

# and
# or
# not


print('Welcome to Pytgon pizza Deliveries');

size = input("what size pizza do you want?S, M or L");

bill = 0;

if size == "S":
    bill += 15
    add_pep = input("Do you want pep? Y or N");
    x_cheez = input("Do you want xtra cheez? Y or N");

    if add_pep == "Y" and x_cheez == "N" :
        bill += 2;
        print(f'total bill is ${bill}');
    elif add_pep == "N" and x_cheez == "Y" :
        bill += 1;
        print(f'total bill is ${bill}');
    elif add_pep == "Y" and x_cheez == "Y":
        bill += 2;
        bill += 1;    
        print(f'total bill is ${bill}');
    else:                
        print(f'total bill is ${bill}');
           
elif size == "M" :
    bill += 20
    add_pep = input("Do you want pep? Y or N");
    x_cheez = input("Do you want xtra cheez? Y or N");

    if add_pep == "Y" and x_cheez == "N" :
        bill += 3;
        print(f'total bill is ${bill}');
    elif add_pep == "N" and x_cheez == "Y" :
        bill += 1;
        print(f'total bill is ${bill}');
    elif add_pep == "Y" and x_cheez == "Y":
        bill += 3;
        bill += 1;    
        print(f'total bill is ${bill}');
    else:                
        print(f'total bill is ${bill}');
  
elif size == "L":
    bill += 25
    add_pep = input("Do you want pep? Y or N");
    x_cheez = input("Do you want xtra cheez? Y or N");

    if add_pep == "Y" and x_cheez == "N" :
        bill += 3;
        print(f'total bill is ${bill}');
    elif add_pep == "N" and x_cheez == "Y" :
        bill += 1;
        print(f'total bill is ${bill}');
    elif add_pep == "Y" and x_cheez == "Y":
        bill += 3;
        bill += 1;    
        print(f'total bill is ${bill}');
    else:                
        print(f'total bill is ${bill}');
else:
    print("Please select the correct size")