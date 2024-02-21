# WAP to check the given two numbers are twin prime or not
import math

num1, num2 = input("Enter Your two number :").split()


def isPrime(number):
    if number <= 1:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


def isTwinPrime(num1, num2):
    if num1 - num2 == 2 or num1 - num2 == -2:
        return True
    else:
        return False


if isPrime(int(num1)) and isPrime(int(num2)):
    if isTwinPrime(int(num1), int(num2)):
        print(f"{num1} and {num2} are twin prime")
    else:
        print(f"{num1} and {num2} are not twin prime")
else:
    print(f"{num1} and {num2} are not prime number")
