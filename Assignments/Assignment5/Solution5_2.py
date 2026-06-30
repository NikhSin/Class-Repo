# 2. Write a program to calculate the sum of all values in the dictionary 
d = {1: 1, 2: 2, 3: 3, 4: 4} 
def sum(d):
    sum_ofkeys=0
    sum_ofvalue=0
    for keys,value in d.items():
        sum_ofkeys+=keys
        sum_ofvalue+=value
    return "Sum of Keys: ",sum_ofkeys,"Sum of values:",sum_ofvalue


res=sum(d)
print(res)