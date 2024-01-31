percentage = float(input("Enter your percentage: "))
if percentage > 90 and percentage <=100:
    print("Your grade is 'O'")
elif percentage > 80 and percentage <=90:
    print("Your grade is 'E'")
elif percentage > 70 and percentage <=80:
    print("Your grade is 'A'")
elif percentage > 60 and percentage <=70:
    print("Your grade is 'B'")
elif percentage > 50 and percentage <=60:
    print("Your grade is 'C'")
elif percentage > 40 and percentage <=50:
    print("Your grade is 'd'")
else:
    print("You fail in exam")
