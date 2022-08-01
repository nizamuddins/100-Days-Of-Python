# if/elif
weight = int(input('Enter weigth'));
height = int(input('Enter height'));

bmi = round(weight/(height**2),2)
if bmi < 18:
        print(f"you are 'underweight' {bmi}");
elif bmi < 25:
    print(f'you have normal weight {bmi}');        
elif bmi < 30:
    print(f'your are overweight {bmi}');
elif bmi < 35:
    print(f'you are obese {bmi}')            
else:
    print(f'you are clinically obese {bmi}')
