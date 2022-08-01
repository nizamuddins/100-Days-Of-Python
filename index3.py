# nested-if/else

print('Welcome to the roller coaster!');

heigth = int(input('What is your height in cm?'));
if heigth>120:
    print('You can ride the rollercoaster');
    age = int(input('Enter age'));
    if age <= 18:
        if age>=15:
            print("$2 for ticket");
        else:
            print('no ticket')
    else:
        print('$35 for ticket')    
else:
    print('Sorry you cant ride'); 