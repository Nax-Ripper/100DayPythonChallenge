
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")


# print(int(float(weight)/(float(height)*float(height))))
bmi = float(weight)/float(height)**2
print(int(bmi))
