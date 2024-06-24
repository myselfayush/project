print("welcome to love calculator just for fun ")
name1 = input("write your name = ")
name2 = input("write others name = ")

add_string = name1 + name2
z = add_string.lower()

T = z.count("t")
R = z.count("r")
U = z.count("u")
E = z.count("e")

TRUE = T + R + U + E

L = z.count("l")
O = z.count("o")
V = z.count("v")
E = z.count("e")

LOVE = L + O + V + E

add = str(TRUE) + str(LOVE)
print(add)
