name1 = input("What is your nme ? : ")
name2 = input("What is your partner name ? : ")

T = 0
R = 0
U = 0
E = 0

L = 0
O = 0
V = 0
E = 0

combined = name1 + name2
lower_names = combined.lower()

T = T + combined.count("t")
R = R + combined.count("r")
U = U + combined.count("u")
E = E + combined.count("e")

sumTrue = T + R + U + E

L = L + combined.count("l")
O = O + combined.count("o")
V = V + combined.count("v")
E = E + combined.count("e")

sumLove = L + O + V + E

score = int(str(sumTrue) + str(sumLove))

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos ")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, You are alright together .")
else:
    print(f"Your score is {score}. ")
