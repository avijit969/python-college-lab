dict = {"a": [1, 1, 1],
        "b": [2, 2, 2],
        "c": [2, 5]}
max_value = 0
unique_key = None
unique_value = None
final = {}

for key, value in dict.items():
    max_len = len(set(value))
    if max_value < max_len:
        max_value = max_len
        unique_key = key
        unique_value = value

final[unique_key] = unique_value
print(final)
