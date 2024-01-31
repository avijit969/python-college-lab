word = input("Enter yor string :").lower()
vowels_count = 0
consonant_count = 0
for char in word:
    if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
        vowels_count += 1
    else:
        consonant_count +=1
print(f"{vowels_count} number of vowels and {consonant_count} number of consonant are present in {word}")
