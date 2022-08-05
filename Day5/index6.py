#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password =  '';

for num1 in range(0,nr_letters):
    letter = random.randint(0,len(letters)-1);
    password += letters[letter];
for num2 in range(0,nr_symbols):
    symbol = random.randint(0,len(symbols)-1);
    password += symbols[symbol]; 
for num3 in range(0,nr_numbers):
    number = random.randint(0,len(numbers)-1);
    password += numbers[number];

# shuffle

# random.shuffle(password);
# password1 = ''.join(password);

password1 = [char for char in password];
random.shuffle(password1);
password3 = "".join(password1);
print(password3);

