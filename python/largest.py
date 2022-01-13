num1 = int(input("Enter number:"))
num2 = int(input("Enter number:"))
num3 = int(input("Enter number:"))
if num1 > num2 and num1 > num3:
    print("{0} is largest".format(num1))
elif num2 > num3 and num2 > num1:
    print("{0} is largest".format(num2))
else:
    print("{0} is largest".format(num3))


