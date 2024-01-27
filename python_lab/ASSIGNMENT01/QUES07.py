m = int(input("Enter your time is minutes: "))
s = 12601
s = s % (24 * 3600)
h = s // 3600
n = s // 60
print(f"{round(h, 2)} : {n}")
