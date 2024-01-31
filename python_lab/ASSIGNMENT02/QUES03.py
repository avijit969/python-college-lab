num = input("Enter your number :")
rev = ""
for i in range(len(num) - 1, -1, -1):
    rev += num[i]

if num == rev:
    print(f"{num} is palindrome number")
else:
    print(f"{num} is not palindrome number")
