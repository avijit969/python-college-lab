# WAP to remove all duplicates from a given string
def remove_duplicate(string):
    str = set()
    result = []

    for char in string:
        if char not in str:
            result.append(char)
            str.add(char)
    finalResult = "".join(result)
    return finalResult


string = input("Enter your string that you want to remove duplicate value :")
print(f"After remove all duplicate value string is {remove_duplicate(string)}")
