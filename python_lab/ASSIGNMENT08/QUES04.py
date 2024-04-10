# WAP to copy the content of a file to another file
file1 = open('word.txt', 'r')
file2 = open('copy.txt', 'w')
file2.write(file1.read())
print("file copied successfully ")