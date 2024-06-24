age = input("enter your current age = ")
age_int = int(age)

remaining = 100 - age_int
days = remaining * 365
week = remaining * 52
year = week / 52

result = (f" days = {days}\n month = {week}\n year = {year}\n")
print(result)