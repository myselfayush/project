''' here we calculation of bmi index tool by using the formula
H = height 
w = weight 

'''
from turtle import right


a = input( "what's your height? ")# type: ignore

b = input(" what's your weight? ") # type: ignore

h = float(a)

w = int(b)

bmi = w / (h * h)
bmi_string = str(bmi)
print ("you bmi index is " + bmi_string)

# now, i finished my code by understand and solving the problem