# WAP to add three given list using python map and lamda
list1 = [1, 2, 3, 4]
list2 = [4, 5, 6, 7]
list3 = [8, 9, 10, 2]

result = list(map(lambda x, y, z: x + y + z, list1, list2, list3))
print(result)