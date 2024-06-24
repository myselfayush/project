print("eligibility check to qualify you to next round")
age = int(input("enter your age = "))
marks = int(input("enter your marks in percentage = "))
if age < 18:
    print("you have to pay 600 in inr = ")
    if marks >= 80:
        print("you are eligible")
    elif age <= 17:
        print("you can pay 650 ")
    else:
        print("you have to pay 1000 in inr = ")
    