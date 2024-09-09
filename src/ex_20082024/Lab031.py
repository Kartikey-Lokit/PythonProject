# find number between 3 number

num1=float(input("Enter the num1\n"))
num2=float(input("Enter the num2\n"))
num3=float(input("Enter the num3\n"))

if num1 > num2 and num1 > num3:
    print(f"Max is {num1}")

    elif num2 > num1 and num2 > num3:
    print(f"max is {num2}")

else
    print(f"Max is {num3}")