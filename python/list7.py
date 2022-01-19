new_list=[1,1,1,2,2,2,3,3,3,4,4,4,5,5,5]
sub_list=[]
for i in range(1,len(new_list)):
    if(new_list[i]==new_list[i-1]):
        sub_list.append([new_list[i],new_list[i]])
print(sub_list)

