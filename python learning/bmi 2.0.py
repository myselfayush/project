height = float(input("enter your height in m = "))
weight = float(input("enter your weight in kg = "))

bmi = round(weight / height ** 2)

if bmi < 18:
    print("you are under weight")
elif bmi < 25:
    print("you are normal")
elif bmi < 30:
    print("you are over weight")
else:
    print("do exercise and more physical activities")