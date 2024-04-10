# 1.	WAP to read last n lines of files.
n = int(input("Enter number of lines to read: "))
with open("text.txt") as file:
    lines = file.readlines()
for i in range(-1, -(n+1), -1):
    print(lines[i])
