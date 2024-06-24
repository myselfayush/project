
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? s, m, or L ")
add_pepperoni = input("Do you want pepperoni? y or n ")
extra_cheese = input("Do you want extra cheese? y or n ")

bill = 0

if size == "s":
    bill += 15

elif size == "m":
    bill += 20

elif size == "l":
    bill += 25

    if add_pepperoni == "y":
            bill += 2
            if extra_cheese == "y":
                                bill += 1
                                print(f"your total bill is $ {bill}")