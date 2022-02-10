range_of_user=int(input("Enter the range of the luckiest number: "))
lucky_num=list(range(1,range_of_user,1))

def get_not_survived_elements(n,numbers):
    elements_not_survived=[]
    for i in range(n-1,len(numbers),n):
        elements_not_survived.append(numbers[i])
    return elements_not_survived   

def delete_not_survived_elements(lucky,removed):
    lucky=set(lucky)
    removed=set(removed)
    new_list=lucky.difference(removed)
    return list(new_list)

def islem(n,lucky_num):
    elements_not_survived=get_not_survived_elements(n,lucky_num)
    removed_2=delete_not_survived_elements(lucky_num,elements_not_survived)
    return removed_2

x=2 
while len(islem(x,lucky_num)) >= x:
    lucky_num = islem(x,lucky_num)
    lucky_num.sort()
    print('x:',x,'numbers:',lucky_num)
    x +=1 

 