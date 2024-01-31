num1, num2, num3  = input("Enter your three number :")
# numbers = numbers.split()
# num1, num2, num3 = numbers
if (num1.isdigit() and num2.isdigit() and num2.isdigit()):
    num1 = int(num1)
    num2 = int(num2)
    num3 = int(num3)
    if (num1 < num2 and num1 < num3):
        print("min number is ", num1)
    elif (num2 < num3):
        print("min number is ", num2)
    else:
        print("min number is ", num3)
else:
    print("Please enter valid input")
