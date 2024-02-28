def print_even(list):
    result=[]
    for i in range(0,len(list)):
        if list[i] %2==0:
            result.append(list[i])
    return result

list=[1,2,3,4,5,6,7,8,9,10,11,23,45,23,13,14,17,18,99,56]
print(print_even(list))