import math
a = int(input("Enter a value of a: "))
b = int(input("Enter a value of b: "))
c = int(input("Enter a value of c: "))
d = b*b-4*a*c
if d<0:
    print("ROOTS are imaginary")
else:
    root1 = (-b+math.sqrt(d))/(2.0*a)
    root2 = (-d-math.sqrt(d))/(2.0*a)
    print("Root1= ",root1)
    print("Root2= ",root2)
