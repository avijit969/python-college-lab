# WAP to count the frequency of word in a file.

with open("word.txt", 'r') as file:
    lines = file.readlines()
print(type(lines))
sentence = "".join(lines)
for word in sentence.split():
    print(f'frequency of { word} is {sentence.count(word)}')
