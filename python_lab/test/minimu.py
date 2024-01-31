num1 = input("Enter your first number:")
if (num1.isdigit()):
    num1 = int(num1)
else:
    print("Please enter valid input")
num2 = input("Enter your 2nd number:")
if (num2.isdigit()):
    num2 = int(num2)
else:
    print("Please enter valid input")
num3 = input("Enter your 3rd number:")
if (num3.isdigit()):
    num3 = int(num3)
else:
    print("Please enter valid input")

if(num1<num2 and num1<num3):
    print("min number is ",num1)
elif(num2<num3 ):
    print("min number is ", num2)
else:
    print("min number is ",num3)
