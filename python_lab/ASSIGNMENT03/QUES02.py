# WAP to find the factorial of a number ?

number = int(input("Enter your number: "))


def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)


print(f"factorial of {number} is {factorial(number)}")
