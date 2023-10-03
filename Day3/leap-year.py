year = int(input("Enter a year "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("This is leap year")
        else:
            print("This is not leap year")
    else:
        print("This is not leap year")
else:
    print("This is not leap year")
