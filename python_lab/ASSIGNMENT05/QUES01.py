# WAP to input two dictionaries and print the values by merging the two dictionaries
dict1 = {}
dict2 = {}
for i in range(0, 4):
    key, value = input("enter key and value separated by space for 1st dict").split()
    dict1[key] = value
for i in range(0, 4):
    key, value = input("enter key and value separated by space for 2st dict").split()
    dict2[key] = value
final_dict = {}
final_dict.update(dict1)
final_dict.update(dict2)
print(final_dict)
