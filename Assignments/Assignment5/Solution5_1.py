import time
#1. Write a program to calculate the sum of all keys in the dictionary 
d = {1: 1, 2: 2, 3: 3, 4: 4} 
# key_sum = sum(d.keys())
# print("Sum of all keys:", key_sum)  
# def sum1(dic):
#     summ=0
#     for keys in dic:
#         summ+=keys
#     return summ    


# res=sum1(d)
# print(res)

def summ(dic):
    s=0
    for keys,value in dic.items():
        s+=keys
    return s

res=summ(d)
print(res)