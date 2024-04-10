# WAP to convert all the characters into uppercase and lowercase and
# eliminate duplicate letters from a given sequence . use map() function
string = "ABhijitPradhan"


def upper_lower(char):
    if char.islower():
        return char.upper()
    elif char.isupper():
        return char.lower()

converted_string = list(map(lambda char: upper_lower(char) , string))
print("".join(list(set(converted_string))))
