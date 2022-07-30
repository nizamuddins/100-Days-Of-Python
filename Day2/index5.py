# BMI Calculator
weight = input('weight?\n');
height = input(('height?\n'));

weight1 = int(weight);
height2 = int(height);

BMI = round(weight1/(height2**2),3);
BMI2 = str(BMI)
print('Your bmi is '+BMI2)