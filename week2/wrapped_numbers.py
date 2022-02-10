w_list=list(input("Input a list with comma:").split(','))
num=int(input("Input a number:"))
def wrap(w_list,num):
    if  num<0:
        num=num-1
        return print(w_list[num:]+w_list[:num])
    elif 0<num<=len(w_list):
        num=num+1
        return print(w_list[num:]+w_list[:num])
    else:
        num=num%len(w_list)
        return print(w_list[num:]+w_list[:num])
wrap(w_list,num)

