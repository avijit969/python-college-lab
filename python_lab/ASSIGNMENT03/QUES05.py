# WAP to print even length words in a string

sentence = input("Enter yor sentence :").split()
print("Even length words are : ")
for word in sentence:
    if (len(word) % 2) == 0:
        print(word)