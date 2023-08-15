print('Welcome to the tip Calculator.')
total_bill=input('What was the total bill? $')
percent = input('What percentage tip would you like to give? 10, 12, or 15? ')
persons=input('How many people to split the bill? ')

percent_int= float(f'1.{percent}')
totl_bill_float= float(total_bill)
persons= float(persons)

# pay = (totl_bill_float+(totl_bill_float*(100-percent_int)))/persons
pay = (totl_bill_float*percent_int)/persons
print(f'Each person should pay: ${round(pay,2)}')
