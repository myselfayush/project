print("welcome to tip calculator")
bill = float(input( "enter your total bills? "))
tips = int(input("enter your tips in %  "))
people = int(input("how manny people to spilt the bill? "))
tip = tips / 100 * bill + bill
tip_amount = tips / 100 * bill
print("your total tips amount" )
print (tip_amount)
print("here is your total amount you have to pay" ) 
print (tip)