print("Thank you for choosing Python Pizza Delivery")

size = input("Enter your size . (L - large , M - medium , S - small)")
pizza_prize = 0
if size == "L":
    pizza_prize = 25
elif size == "M":
    pizza_prize = 20
elif size == "S":
    pizza_prize = 15

peperoni = input("Add peperoni for pizza (Y or N) : ")
if peperoni == "Y":
    pizza_prize = pizza_prize + 3
cheese = input("Add extra cheese ? (Y or N)")
if cheese == "Y":
    pizza_prize = pizza_prize + 1

print(
        f"Thank your for choosing python pizza delivery! Your final  bill is :$ {pizza_prize}"
    )
