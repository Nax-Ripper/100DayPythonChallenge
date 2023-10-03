print("Welcome to the rollercoaster")
height = int(input("What is your height in cm ?"))
totalBil = 0


if height > 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))

    if age < 12:
        print("please pay $5. ")
        totalBil = 5

    elif age <= 18:
        print("please pay $7. ")
        totalBil = 7
    elif age >= 45 and age <= 55:
        print("Free")
        totalBil = 0
    else:
        print("Please pay $12.")
        totalBil = 12

    photo = input("Want photos ? Type yes or no : ")
    if photo == "yes":
        totalBil = totalBil + 3
        print(f"Your total bill is {totalBil}")

    else:
        print(f"Your total bill is {totalBil}")
else:
    print("Sorry, You have to grow taller before you can ride")
