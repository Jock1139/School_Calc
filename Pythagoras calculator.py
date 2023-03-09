from math import sqrt
#Imports the math module sqrt
print("Input lengths of shorter triangle sides:")
a = float(input("a: "))
b = float(input("b: "))
#Our input which can be decimals and so on

c = sqrt(a**2 + b**2)
round(c,2)
#Rounds c to 2 decimals
print("The length of the hypotenuse is", round(c,2))

