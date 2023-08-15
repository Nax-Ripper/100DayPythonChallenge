# 1 year =365 days
# 1 year = 52 weeks
# 1 year = 12 months

curr_age = input('What is your current age? ')

total_year =90

remaining_year = total_year-int(curr_age)

in_months = remaining_year*12
in_weeks = remaining_year*52
in_days = remaining_year*365

print(f'You have {in_days} days, {in_weeks} weeks, and {in_months} months left.')