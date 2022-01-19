list=[1,1,1,2,2,3,3,5,5,4,4,6,6,8,8,9]
i=0
while i<len(list)-1:
    if list[i] == list[i+1]:
        del list[i]
    else:
        i=i+1
print("The list is",list)
