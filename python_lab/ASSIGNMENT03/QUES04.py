# WAP to check whether the string is symmetrical or palindrome ?
word = input("Enter your string : ")
if word == word[::-1] :
    print(f"{word} is symmetrical or palindrome string")
else:
    print(f"{word} is not symmetrical or palindrome string")