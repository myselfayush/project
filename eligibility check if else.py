# eligibility criteria = age must be 18 or above 18 | your cgp must br equal to or above 8 
print(" welcome to coding competition")

age = int(input("what is your age? "))

cgpa = float(input("what is your cgpa? "))

if age >= 18:
    print("successfully passed aged eligibility criteria")
else:
    print("age eligibilty criteria not passed")

if cgpa >= 8:
    print("successfully passed cgpa eligibility criteria")
else:
    print("your cgpa not enough to join this programme")
