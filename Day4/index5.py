row1 = ['⬜️ ','⬜️ ','⬜️ '];
row2 = ['⬜️ ','⬜️ ','⬜️ '];
row3 = ['⬜️ ','⬜️ ','⬜️ '];



list = [row1,row2,row3];

print(f'{row1}\n{row2}\n{row3}');

print('Where do you want to put the treasure?');
position = input('enter the column number and row number: ');
values = position;
if values <= '22':
    list[int(values[1])][int(values[0])] = 'x';
    print(f'{row1}\n{row2}\n{row3}');

else:
    print('Enter positive number')
