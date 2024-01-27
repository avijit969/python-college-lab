import math
a = int(input("Enter your 1st 'a' coefficient of a quadratic equation :"))
b = int(input("Enter your 2nd 'b' coefficient of a quadratic equation :"))
c = int(input("Enter your 3rd 'c' coefficient of a quadratic equation :"))

d = int(math.pow(b,2)-(4*a*c))
root1 = (-b-math.sqrt(d))/(2*a)
root2 = (-b+math.sqrt(d))/(2*a)

print(f"roots of the quadratic equation are {root1} and {root2}")
