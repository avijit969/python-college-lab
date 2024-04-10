# WAP to read a file line by line and store in into a list.

with open("text.txt", 'r') as file:
    lines = file.readlines()

print(lines)
