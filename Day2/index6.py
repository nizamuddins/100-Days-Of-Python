# Tip Calculator

bill1 = input("What was the bill?$");
tip = input('What percentage tip would you like to give me? 10, 12 or 15? ');
split = input('How many people to split the bill?');
percent = (int(tip)*float(bill1))/100;

total = float(bill1)+ percent;

each1 = (total)/int(split)
each = "{:.3f}".format(each1)
print(f"Each peson should pay: ${each}")


