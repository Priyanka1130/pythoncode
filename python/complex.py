import cmath 
#num = 1+2j
num = eval(input('Enter a number:'))
num_sqrt = cmath.sqrt(num)
print('The sqaure root of {0} is {1:f}+{2:f}j'.format(num ,num_sqrt.real,num_sqrt.imag))
