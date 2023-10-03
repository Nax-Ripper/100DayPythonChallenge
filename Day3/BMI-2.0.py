

height =  float(input('Enter your height(m) : '))

weight =  int(input('Enter your weight(kg) :  '))

bmi = float(weight/(height**2))

print(f'\nYour bmi is {bmi},')
if(bmi < 18.5):
    print('You are underweight')
elif (bmi <25):
    print('You are normal weight')
elif (bmi <30):
    print('You are slightly overweight')
elif(bmi<35):
    print('You are obese')
else:
    print('You are clinically obese')


