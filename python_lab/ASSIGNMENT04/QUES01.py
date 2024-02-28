# wap to print the second largest and second smallest element in a list of 10 integer without using sort function.
list =[1,2,3,4,5,10]
list.remove(max(list))
list.remove(min(list))
print(f"second largest element is {max(list)}")
print(f"second smallest element is {min(list)}")