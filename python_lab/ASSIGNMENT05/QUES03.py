dict = {"a": "1",
        "b": 2,
        "c": 2,
        "e": 2,
        "f":"1"}
final = {}
for key, value in dict.items():
    if value not in final.values():
        final[key] = value
print(final)
