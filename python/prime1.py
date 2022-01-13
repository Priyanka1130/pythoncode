num = int(input("Enter a number:"))
flag = False
if num > 1:
    for i in range (2,num):
        if num%i == 0:
            flag = True
            break
if flag:
    print("is not prime number",num)
else:
    print("is prime number",num)
