num = int(input("Enter 3-digit number: "))
numberOfPrimeFactor = 0

for i in range(1, num + 1):
    if num % i == 0:
        is_prime = True
        for j in range(2, int(i /2) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime and i > 1:
            print(i)
            numberOfPrimeFactor += 1

print("Number of prime factors:", numberOfPrimeFactor)
