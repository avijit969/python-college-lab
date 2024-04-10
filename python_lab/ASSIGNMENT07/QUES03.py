# WAP to create a list containing power of said
import math

num = [1, 2, 3, 4, 5]
power_list = [2, 2, 3, 4, 5]

result = list(map(lambda x, p: math.pow(x, p), num, power_list))
print(result)
