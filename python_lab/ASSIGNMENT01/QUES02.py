import math

a = int(input("enter your 1st side 'a' : "))
b = int(input("enter your 2nd side 'b' : "))
c = int(input("enter your 3rd side 'c' : "))
s = (a + b + c) / 2
area = math.sqrt(s * (s - a) * (s - b) * (s - c))

print("Area of the triangle is :", area)
